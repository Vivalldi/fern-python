import fern.ir.pydantic as ir_types
from generator_exec.resources import GeneratorConfig

from fern_python.codegen import Filepath

from ..declaration_referencers import ServiceDeclarationReferencer
from .fastapi_generator_context import FastApiGeneratorContext


class FastApiGeneratorContextImpl(FastApiGeneratorContext):
    def __init__(self, ir: ir_types.IntermediateRepresentation, generator_config: GeneratorConfig):
        super().__init__(ir=ir, generator_config=generator_config)
        self._service_declaration_handler = ServiceDeclarationReferencer(
            generator_config=generator_config,
            ir=ir,
        )

    def get_filepath_for_service(self, service_name: ir_types.services.DeclaredServiceName) -> Filepath:
        return self._service_declaration_handler.get_filepath(name=service_name)
