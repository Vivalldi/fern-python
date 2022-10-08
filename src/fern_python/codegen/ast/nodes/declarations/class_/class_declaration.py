from __future__ import annotations

from typing import List, Sequence, Set

from ....ast_node import AstNode, GenericTypeVar, NodeWriter, ReferenceResolver
from ....references import ClassReference, Module, Reference, ReferenceImport
from ...code_writer import CodeWriter
from ...expressions import Expression
from ...reference_node import ReferenceNode
from ..function import FunctionDeclaration, FunctionParameter, FunctionSignature
from ..variable import VariableDeclaration
from .class_constructor import ClassConstructor
from .class_method_decorator import ClassMethodDecorator


class ClassDeclaration(AstNode):
    def __init__(
        self,
        name: str,
        is_abstract: bool = False,
        extends: Sequence[ClassReference] = None,
        constructor: ClassConstructor = None,
        docstring: str = None,
    ):
        self.name = name
        self.extends = list(extends or [])
        if is_abstract:
            self.extends.insert(
                0,
                ClassReference(
                    qualified_name_excluding_import=("ABC",),
                    import_=ReferenceImport(module=Module.built_in("abc")),
                ),
            )
        self.constructor = constructor
        self.docstring = docstring
        self.statements: List[AstNode] = []
        self.ghost_references: Set[Reference] = set()

    def add_class_var(self, variable_declaration: VariableDeclaration) -> None:
        self.statements.append(variable_declaration)

    def add_method(
        self,
        declaration: FunctionDeclaration,
        decorator: ClassMethodDecorator = None,
        no_implicit_decorator: bool = False,
    ) -> FunctionDeclaration:
        def augment_signature(signature: FunctionSignature) -> FunctionSignature:
            parameters = (
                signature.parameters
                if decorator == ClassMethodDecorator.STATIC
                else [FunctionParameter(name="cls")] + list(signature.parameters)
                if decorator == ClassMethodDecorator.CLASS_METHOD
                else [FunctionParameter(name="self")] + list(signature.parameters)
            )

            return FunctionSignature(
                parameters=parameters,
                named_parameters=signature.named_parameters,
                return_type=signature.return_type,
                include_args=signature.include_args,
                include_kwargs=signature.include_kwargs,
            )

        decorators = (
            list(declaration.decorators)
            + [ReferenceNode(Reference(qualified_name_excluding_import=(decorator.value,)))]
            if decorator is not None and not no_implicit_decorator
            else declaration.decorators
        )

        declaration = FunctionDeclaration(
            name=declaration.name,
            signature=augment_signature(declaration.signature),
            body=declaration.body,
            decorators=decorators,
            overloads=[augment_signature(overload) for overload in declaration.overloads],
        )

        self.statements.append(declaration)

        return declaration

    def add_abstract_method(
        self,
        name: str,
        signature: FunctionSignature,
    ) -> FunctionDeclaration:
        return self.add_method(
            declaration=FunctionDeclaration(
                name=name,
                signature=signature,
                body=CodeWriter("..."),
                decorators=[
                    ReferenceNode(
                        Reference(
                            qualified_name_excluding_import=("abstractmethod",),
                            import_=ReferenceImport(module=Module.built_in("abc")),
                        )
                    )
                ],
            )
        )

    def add_class(self, declaration: ClassDeclaration) -> None:
        self.statements.append(declaration)

    def add_ghost_reference(self, reference: Reference) -> None:
        self.ghost_references.add(reference)

    def get_references(self) -> Set[Reference]:
        references: Set[Reference] = {*self.extends, *self.ghost_references}
        if self.constructor is not None:
            references.update(self.constructor.get_references())
        for statement in self.statements:
            references.update(statement.get_references())
        return references

    def get_generics(self) -> Set[GenericTypeVar]:
        generics: Set[GenericTypeVar] = set()
        if self.constructor is not None:
            generics.update(self.constructor.get_generics())
        for statement in self.statements:
            generics.update(statement.get_generics())
        return generics

    def add_expression(self, expression: Expression) -> None:
        self.statements.append(expression)

    def write(self, writer: NodeWriter, reference_resolver: ReferenceResolver) -> None:
        top_line = f"class {self.name}"
        if len(self.extends) > 0:
            top_line += f"({', '.join(reference_resolver.resolve_reference(r) for r in self.extends)})"
        top_line += ":"
        writer.write_line(top_line)

        with writer.indent():
            if self.docstring is not None:
                trimmed_docstring = self.docstring.strip()
                if len(trimmed_docstring) > 0:
                    writer.write_line(f'"""\n{trimmed_docstring}\n"""')
            for statement in self.statements:
                writer.write_node(statement)
                writer.write_newline_if_last_line_not()
            if len(self.statements) == 0:
                writer.write("pass")
            writer.write_line()
