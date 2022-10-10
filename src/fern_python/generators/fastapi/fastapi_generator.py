import fern.ir.pydantic as ir_types
from generator_exec.resources import GeneratorConfig

from fern_python.cli.abstract_generator import AbstractGenerator
from fern_python.codegen import Project
from fern_python.generator_exec_wrapper import GeneratorExecWrapper
from fern_python.generators.pydantic_model import (
    PydanticModelCustomConfig,
    PydanticModelGenerator,
)
from fern_python.source_file_generator import SourceFileGenerator

from .auth import SecurityFileGenerator
from .context import FastApiGeneratorContext, FastApiGeneratorContextImpl
from .service_generator import ServiceGenerator


class FastApiGenerator(AbstractGenerator):
    def run(
        self,
        *,
        generator_exec_wrapper: GeneratorExecWrapper,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
        project: Project,
    ) -> None:
        context = FastApiGeneratorContextImpl(ir=ir, generator_config=generator_config)
        PydanticModelGenerator().generate_types(
            generator_exec_wrapper=generator_exec_wrapper,
            custom_config=PydanticModelCustomConfig.parse_obj({}),
            ir=ir,
            project=project,
            context=context.pydantic_generator_context,
        )

        for service in ir.services.http:
            self._generate_service(
                context=context,
                ir=ir,
                generator_exec_wrapper=generator_exec_wrapper,
                service=service,
                project=project,
            )

        SecurityFileGenerator(context=context).generate_security_file(
            project=project, generator_exec_wrapper=generator_exec_wrapper
        )

        context.core_utilities.copy_to_project(project=project)

    def _generate_service(
        self,
        context: FastApiGeneratorContext,
        ir: ir_types.IntermediateRepresentation,
        generator_exec_wrapper: GeneratorExecWrapper,
        service: ir_types.services.HttpService,
        project: Project,
    ) -> None:
        filepath = context.get_filepath_for_service(service.name)
        with SourceFileGenerator.generate(
            project=project, filepath=filepath, generator_exec_wrapper=generator_exec_wrapper
        ) as source_file:
            ServiceGenerator(context=context, service=service).generate(source_file=source_file)
