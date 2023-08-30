from typing import Optional, Sequence, Tuple

import fern.ir.resources as ir_types
from fern.generator_exec.resources.config import GeneratorConfig
from fern.generator_exec.resources.readme import BadgeType, GenerateReadmeRequest

from fern_python.cli.abstract_generator import AbstractGenerator
from fern_python.codegen import Project
from fern_python.codegen.filepath import Filepath
from fern_python.generator_exec_wrapper import GeneratorExecWrapper
from fern_python.generators.pydantic_model import (
    PydanticModelCustomConfig,
    PydanticModelGenerator,
)
from fern_python.generators.sdk.context.sdk_generator_context import SdkGeneratorContext
from fern_python.generators.sdk.context.sdk_generator_context_impl import (
    SdkGeneratorContextImpl,
)
from fern_python.generators.sdk.core_utilities.client_wrapper_generator import (
    ClientWrapperGenerator,
)
from fern_python.source_file_generator import SourceFileGenerator

from .client_generator.client_generator import ClientGenerator
from .client_generator.root_client_generator import (
    GeneratedRootClient,
    RootClientGenerator,
)
from .custom_config import SDKCustomConfig
from .environment_generators import (
    GeneratedEnvironment,
    MultipleBaseUrlsEnvironmentGenerator,
    SingleBaseUrlEnvironmentGenerator,
)
from .error_generator.error_generator import ErrorGenerator


class SdkGenerator(AbstractGenerator):
    def should_format_files(
        self,
        *,
        generator_config: GeneratorConfig,
    ) -> bool:
        custom_config = SDKCustomConfig.parse_obj(generator_config.custom_config or {})
        return not custom_config.skip_formatting

    def get_relative_path_to_project_for_publish(
        self,
        *,
        generator_config: GeneratorConfig,
        ir: ir_types.IntermediateRepresentation,
    ) -> Tuple[str, ...]:
        custom_config = SDKCustomConfig.parse_obj(generator_config.custom_config or {})
        if custom_config.package_name is not None:
            return (custom_config.package_name,)
        return (
            (
                generator_config.organization,
                ir.api_name.snake_case.unsafe_name,
            )
            if custom_config.use_api_name_in_package
            else (generator_config.organization,)
        )

    def run(
        self,
        *,
        generator_exec_wrapper: GeneratorExecWrapper,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
        project: Project,
    ) -> None:
        custom_config = SDKCustomConfig.parse_obj(generator_config.custom_config or {})

        if not custom_config.client_filename.endswith(".py"):
            raise RuntimeError("client_filename must end in .py")

        self._pydantic_model_custom_config = PydanticModelCustomConfig(
            wrapped_aliases=custom_config.wrapped_aliases,
            skip_formatting=custom_config.skip_formatting,
            include_union_utils=custom_config.include_union_utils,
            orm_mode=False,
            frozen=True,
            smart_union=True,
        )

        context = SdkGeneratorContextImpl(
            ir=ir,
            generator_config=generator_config,
            custom_config=custom_config,
            project=project,
        )

        PydanticModelGenerator().generate_types(
            generator_exec_wrapper=generator_exec_wrapper,
            custom_config=self._pydantic_model_custom_config,
            ir=ir,
            project=project,
            context=context.pydantic_generator_context,
        )

        generated_environment: Optional[GeneratedEnvironment] = None
        if ir.environments is not None:
            generated_environment = self._generate_environments(
                context=context,
                environments=ir.environments.environments,
                generator_exec_wrapper=generator_exec_wrapper,
                project=project,
            )

        self._generate_client_wrapper(
            context=context,
            generated_environment=generated_environment,
            generator_exec_wrapper=generator_exec_wrapper,
            project=project,
        )

        generated_root_client = self._generate_root_client(
            context=context,
            ir=ir,
            generated_environment=generated_environment,
            generator_exec_wrapper=generator_exec_wrapper,
            project=project,
        )

        for subpackage_id in ir.subpackages.keys():
            subpackage = ir.subpackages[subpackage_id]
            if subpackage.has_endpoints_in_tree:
                self._generate_subpackage_client(
                    context=context,
                    ir=ir,
                    generator_exec_wrapper=generator_exec_wrapper,
                    subpackage_id=subpackage_id,
                    subpackage=subpackage,
                    project=project,
                )

        for error in ir.errors.values():
            self._generate_error(
                context=context,
                ir=ir,
                generator_exec_wrapper=generator_exec_wrapper,
                error=error,
                project=project,
            )

        context.core_utilities.copy_to_project(project=project)

        output_mode = generator_config.output.mode.get_as_union()
        if output_mode.type == "github":
            request_sent = self._generate_readme(
                generator_exec_wrapper=generator_exec_wrapper,
                generated_root_client=generated_root_client,
                capitalized_org_name=generator_config.organization.capitalize(),
                project=project,
            )
            if request_sent:
                project.set_generate_readme(False)

    def _generate_environments(
        self,
        context: SdkGeneratorContext,
        environments: ir_types.Environments,
        generator_exec_wrapper: GeneratorExecWrapper,
        project: Project,
    ) -> GeneratedEnvironment:
        filepath = context.get_filepath_for_environments_enum()
        with SourceFileGenerator.generate(
            project=project, filepath=filepath, generator_exec_wrapper=generator_exec_wrapper
        ) as source_file:
            return environments.visit(
                single_base_url=lambda single_base_url_environments: SingleBaseUrlEnvironmentGenerator(
                    context=context, environments=single_base_url_environments
                ).generate(source_file=source_file),
                multiple_base_urls=lambda multiple_base_urls_environments: MultipleBaseUrlsEnvironmentGenerator(
                    context=context, environments=multiple_base_urls_environments
                ).generate(source_file=source_file),
            )

    def _generate_client_wrapper(
        self,
        context: SdkGeneratorContext,
        generated_environment: Optional[GeneratedEnvironment],
        generator_exec_wrapper: GeneratorExecWrapper,
        project: Project,
    ) -> None:
        filepath = Filepath(
            directories=context.core_utilities.filepath,
            file=Filepath.FilepathPart(module_name="client_wrapper"),
        )
        with SourceFileGenerator.generate(
            project=project,
            filepath=filepath,
            generator_exec_wrapper=generator_exec_wrapper,
        ) as source_file:
            ClientWrapperGenerator(
                context=context,
                generated_environment=generated_environment,
            ).generate(source_file=source_file, project=project)

    def _generate_root_client(
        self,
        context: SdkGeneratorContext,
        ir: ir_types.IntermediateRepresentation,
        generated_environment: Optional[GeneratedEnvironment],
        generator_exec_wrapper: GeneratorExecWrapper,
        project: Project,
    ) -> GeneratedRootClient:
        with SourceFileGenerator.generate(
            project=project,
            filepath=context.get_filepath_for_root_client(),
            generator_exec_wrapper=generator_exec_wrapper,
        ) as source_file:
            return RootClientGenerator(
                context=context,
                package=ir.root_package,
                generated_environment=generated_environment,
                class_name=context.get_class_name_for_root_client(),
                async_class_name="Async" + context.get_class_name_for_root_client(),
            ).generate(source_file=source_file)

    def _generate_subpackage_client(
        self,
        context: SdkGeneratorContext,
        ir: ir_types.IntermediateRepresentation,
        generator_exec_wrapper: GeneratorExecWrapper,
        subpackage_id: ir_types.SubpackageId,
        subpackage: ir_types.Subpackage,
        project: Project,
    ) -> None:
        filepath = context.get_filepath_for_subpackage_service(subpackage_id)
        with SourceFileGenerator.generate(
            project=project, filepath=filepath, generator_exec_wrapper=generator_exec_wrapper
        ) as source_file:
            ClientGenerator(
                context=context,
                package=subpackage,
                class_name=context.get_class_name_of_subpackage_service(subpackage_id),
                async_class_name=context.get_class_name_of_async_subpackage_service(subpackage_id),
            ).generate(source_file=source_file)

    def _generate_error(
        self,
        context: SdkGeneratorContext,
        ir: ir_types.IntermediateRepresentation,
        generator_exec_wrapper: GeneratorExecWrapper,
        error: ir_types.ErrorDeclaration,
        project: Project,
    ) -> None:
        filepath = context.get_filepath_for_error(error.name)
        with SourceFileGenerator.generate(
            project=project, filepath=filepath, generator_exec_wrapper=generator_exec_wrapper
        ) as source_file:
            ErrorGenerator(context=context, error=error).generate(source_file=source_file)

    def _generate_readme(
        self,
        generator_exec_wrapper: GeneratorExecWrapper,
        generated_root_client: GeneratedRootClient,
        capitalized_org_name: str,
        project: Project,
    ) -> bool:
        return generator_exec_wrapper.generate_readme(
            self._new_generate_readme_request(
                generated_root_client=generated_root_client,
                capitalized_org_name=capitalized_org_name,
                project=project,
            ),
        )

    def _new_generate_readme_request(
        self,
        generated_root_client: GeneratedRootClient,
        capitalized_org_name: str,
        project: Project,
    ) -> GenerateReadmeRequest:
        badge: Optional[BadgeType] = None
        installation: Optional[str] = None
        if project._project_config is not None:
            badge = BadgeType.PYPI
            installation = f"""```sh
pip install --upgrade {project._project_config.package_name}
```"""

        return GenerateReadmeRequest(
            title=f"{capitalized_org_name} Python Library",
            badge=badge,
            summary=f"The {capitalized_org_name} Python Library provides convenient access to the {capitalized_org_name} API from applications written in Python.",
            installation=installation,
            usage=generated_root_client.usage,
            async_usage=generated_root_client.async_usage,
            requirements=[],
        )

    def get_sorted_modules(self) -> Sequence[str]:
        # always import types/errors before resources (nested packages)
        # to avoid issues with circular imports
        return [".types", ".errors", ".resources"]

    def is_flat_layout(
        self,
        *,
        generator_config: GeneratorConfig,
    ) -> bool:
        custom_config = SDKCustomConfig.parse_obj(generator_config.custom_config or {})
        return custom_config.flat_layout
