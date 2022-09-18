from typing import Set

from fern_python.codegen import AST, SourceFile
from fern_python.declaration_handler import (
    DeclarationHandlerContext,
    HashableDeclaredTypeName,
)
from fern_python.generated import ir_types

from .type_name_to_class_reference_converter import TypeNameToClassReferenceConverter
from .type_reference_to_type_hint_converter import TypeReferenceToTypeHintConverter


class DeclarationHandlerContextImpl(DeclarationHandlerContext):
    def __init__(self, source_file: SourceFile, intermediate_representation: ir_types.IntermediateRepresentation):
        super().__init__(source_file=source_file)
        self._type_reference_to_type_hint_converter = TypeReferenceToTypeHintConverter(
            api_name=intermediate_representation.api_name
        )
        self._type_name_to_class_reference_converter = TypeNameToClassReferenceConverter(
            api_name=intermediate_representation.api_name
        )

        self._type_name_to_declaration = {
            HashableDeclaredTypeName.of(declaration.name): set(
                map(HashableDeclaredTypeName.of, declaration.referenced_types)
            )
            for declaration in intermediate_representation.types
        }

    def get_type_hint_for_type_reference(
        self,
        type_reference: ir_types.TypeReference,
        import_constraint: AST.ImportConstraint = None,
    ) -> AST.TypeHint:
        return self._type_reference_to_type_hint_converter.get_type_hint_for_type_reference(
            type_reference,
            import_constraint=import_constraint,
        )

    def get_class_reference_for_type_name(
        self,
        type_name: ir_types.DeclaredTypeName,
    ) -> AST.ClassReference:
        return self._type_name_to_class_reference_converter.get_class_reference_for_type_name(type_name)

    def get_referenced_types(self, type_name: ir_types.DeclaredTypeName) -> Set[HashableDeclaredTypeName]:
        return self._type_name_to_declaration[HashableDeclaredTypeName.of(type_name)]
