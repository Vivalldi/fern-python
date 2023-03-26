import re

import fern.ir.pydantic as ir_types
from fern.generator_exec.sdk.resources.config import GeneratorConfig

from fern_python.cli.abstract_generator import AbstractGenerator
from fern_python.codegen import Project
from fern_python.generator_exec_wrapper import GeneratorExecWrapper
from fern_python.generators.pydantic_model import (
    PydanticModelCustomConfig,
    PydanticModelGenerator,
)
from fern_python.generators.sdk.context.sdk_generator_context import SdkGeneratorContext
from fern_python.generators.sdk.context.sdk_generator_context_impl import (
    SdkGeneratorContextImpl,
)
from fern_python.source_file_generator import SourceFileGenerator

from .client_generator.client_generator import ClientGenerator
from .custom_config import SDKCustomConfig
from .environment_generator.environment_generator import EnvironmentGenerator
from .error_generator.error_generator import ErrorGenerator


class SdkGenerator(AbstractGenerator):
    def should_format_files(
        self,
        *,
        generator_config: GeneratorConfig,
    ) -> bool:
        custom_config = SDKCustomConfig.parse_obj(generator_config.custom_config or {})
        return not custom_config.skip_formatting

    def run(
        self,
        *,
        generator_exec_wrapper: GeneratorExecWrapper,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
        project: Project,
    ) -> None:
        custom_config = SDKCustomConfig.parse_obj(generator_config.custom_config or {})
        self._pydantic_model_custom_config = PydanticModelCustomConfig(
            wrapped_aliases=custom_config.wrapped_aliases,
            skip_formatting=custom_config.skip_formatting,
        )

        context = SdkGeneratorContextImpl(
            ir=ir,
            generator_config=generator_config,
            client_class_name=(
                custom_config.client_class_name
                or (pascal_case(generator_config.organization) + pascal_case(generator_config.workspace_name))
            ),
            folders_inside_src=(
                [snake_case(custom_config.client_class_name)]
                if custom_config.client_class_name is not None
                else [snake_case(generator_config.organization), snake_case(generator_config.workspace_name)]
            ),
        )

        PydanticModelGenerator().generate_types(
            generator_exec_wrapper=generator_exec_wrapper,
            custom_config=self._pydantic_model_custom_config,
            ir=ir,
            project=project,
            context=context.pydantic_generator_context,
        )

        if ir.environments is not None:
            self._generate_environments(
                context=context,
                environments=ir.environments.environments,
                generator_exec_wrapper=generator_exec_wrapper,
                project=project,
            )

        self._generate_root_client(
            context=context,
            ir=ir,
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

    def _generate_environments(
        self,
        context: SdkGeneratorContext,
        environments: ir_types.Environments,
        generator_exec_wrapper: GeneratorExecWrapper,
        project: Project,
    ) -> None:
        filepath = context.get_filepath_for_environments_enum()
        with SourceFileGenerator.generate(
            project=project, filepath=filepath, generator_exec_wrapper=generator_exec_wrapper
        ) as source_file:
            EnvironmentGenerator(context=context, environments=environments).generate(source_file=source_file)

    def _generate_root_client(
        self,
        context: SdkGeneratorContext,
        ir: ir_types.IntermediateRepresentation,
        generator_exec_wrapper: GeneratorExecWrapper,
        project: Project,
    ) -> None:
        with SourceFileGenerator.generate(
            project=project,
            filepath=context.get_filepath_for_root_client(),
            generator_exec_wrapper=generator_exec_wrapper,
        ) as source_file:
            ClientGenerator(
                context=context,
                package=ir.root_package,
                class_name=context.get_class_name_for_root_client(),
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


def pascal_case(x: str) -> str:
    return "".join(char for char in x.title() if not x.isspace())


# https://stackoverflow.com/a/1176023/4238485
snake_case_pattern = re.compile(r"(?<!^)(?=[A-Z])")


def snake_case(x: str) -> str:
    return snake_case_pattern.sub("_", x).lower()
