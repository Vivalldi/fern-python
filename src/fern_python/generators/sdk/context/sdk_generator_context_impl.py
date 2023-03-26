import fern.ir.pydantic as ir_types
from generator_exec.resources import GeneratorConfig

from fern_python.codegen import AST
from fern_python.codegen.filepath import Filepath

from ..declaration_referencers import (
    EnvironmentsEnumDeclarationReferencer,
    ErrorDeclarationReferencer,
    SubpackageServiceDeclarationReferencer,
)
from .sdk_generator_context import SdkGeneratorContext


class SdkGeneratorContextImpl(SdkGeneratorContext):
    def __init__(
        self,
        *,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
        client_class_name: str,
    ):
        super().__init__(ir=ir, generator_config=generator_config)
        self._error_declaration_referencer = ErrorDeclarationReferencer(filepath_creator=self.filepath_creator)
        self._environments_enum_declaration_referencer = EnvironmentsEnumDeclarationReferencer(
            filepath_creator=self.filepath_creator, client_class_name=client_class_name
        )
        self._subpackage_service_declaration_referencer = SubpackageServiceDeclarationReferencer(
            filepath_creator=self.filepath_creator
        )

    def get_filepath_for_error(self, error_name: ir_types.DeclaredErrorName) -> Filepath:
        return self._error_declaration_referencer.get_filepath(name=error_name)

    def get_class_name_for_error(self, error_name: ir_types.DeclaredErrorName) -> str:
        return self._error_declaration_referencer.get_class_name(name=error_name)

    def get_filepath_for_environments_enum(self) -> Filepath:
        return self._environments_enum_declaration_referencer.get_filepath(name=None)

    def get_reference_to_environments_enum(self) -> AST.ClassReference:
        return self._environments_enum_declaration_referencer.get_class_reference(name=None)

    def get_filepath_for_subpackage_service(self, subpackage_id: ir_types.SubpackageId) -> Filepath:
        subpackage = self.ir.subpackages[subpackage_id]
        return self._subpackage_service_declaration_referencer.get_filepath(name=subpackage)

    def get_class_name_of_subpackage_service(self, subpackage_id: ir_types.SubpackageId) -> str:
        subpackage = self.ir.subpackages[subpackage_id]
        return self._subpackage_service_declaration_referencer.get_class_name(name=subpackage)

    def get_reference_to_error(self, error_name: ir_types.DeclaredErrorName) -> AST.ClassReference:
        return self._error_declaration_referencer.get_class_reference(name=error_name)
