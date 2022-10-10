from abc import ABC, abstractmethod

import fern.ir.pydantic as ir_types
from generator_exec.resources import GeneratorConfig

from fern_python.codegen import Filepath
from fern_python.generators.pydantic_model import PydanticGeneratorContextImpl

from ..core_utilities import CoreUtilities
from ..declaration_referencers import TypeDeclarationReferencer
from ..fastapi_filepath_creator import FastApiFilepathCreator


class FastApiGeneratorContext(ABC):
    def __init__(
        self,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
    ):
        self.ir = ir
        self.generator_config = generator_config
        self.filepath_creator = FastApiFilepathCreator(ir=ir, generator_config=generator_config)
        self.pydantic_generator_context = PydanticGeneratorContextImpl(
            intermediate_representation=ir,
            type_declaration_referencer=TypeDeclarationReferencer(filepath_creator=self.filepath_creator),
        )
        self.core_utilities = CoreUtilities(filepath_creator=self.filepath_creator)

    @abstractmethod
    def get_filepath_for_service(self, service_name: ir_types.services.DeclaredServiceName) -> Filepath:
        ...

    @abstractmethod
    def get_class_name_for_service(self, service_name: ir_types.services.DeclaredServiceName) -> str:
        ...
