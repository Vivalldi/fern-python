from __future__ import annotations

from typing import List, Sequence, Set

from ....ast_node import AstNode, NodeWriter, ReferenceResolver
from ....references import ClassReference, Reference
from ...code_writer import CodeWriter
from ...type_hint import TypeHint
from ..function import FunctionDeclaration, FunctionParameter
from ..variable import VariableDeclaration
from .class_constructor import ClassConstructor


class ClassDeclaration(AstNode):
    def __init__(self, name: str, extends: Sequence[ClassReference] = None, constructor: ClassConstructor = None):
        self.name = name
        self.extends = extends or []
        self.constructor = constructor
        self.statements: List[AstNode] = []

    def add_attribute(self, variable_declaration: VariableDeclaration) -> None:
        self.statements.append(variable_declaration)

    def add_method(
        self, name: str, return_type: TypeHint, parameters: List[FunctionParameter], body: CodeWriter
    ) -> None:
        self.statements.append(
            FunctionDeclaration(
                name=name,
                return_type=return_type,
                parameters=[FunctionParameter(name="self")] + parameters,
                body=body,
            )
        )

    def add_class(self, declaration: ClassDeclaration) -> None:
        self.statements.append(declaration)

    def get_references(self) -> Set[Reference]:
        references: Set[Reference] = set(self.extends)
        if self.constructor is not None:
            references = references.union(self.constructor.get_references())
        for statement in self.statements:
            references = references.union(statement.get_references())
        return references

    def write(self, writer: NodeWriter, reference_resolver: ReferenceResolver) -> None:
        top_line = f"class {self.name}"
        if len(self.extends) > 0:
            top_line += f"({', '.join(reference_resolver.resolve_reference(r) for r in self.extends)})"
        top_line += ":"
        writer.write_line(top_line)

        with writer.indent():
            for statement in self.statements:
                writer.write_node(statement)
            if len(self.statements) == 0:
                writer.write_line("pass\n")
