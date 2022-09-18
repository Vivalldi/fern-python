from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict, Optional, Sequence, Set

from . import AST
from .reference_resolver_impl import ReferenceResolverImpl
from .top_level_statement import StatementId, TopLevelStatement


@dataclass(frozen=True)
class StatementIdAndConstraint:
    statement_id: StatementId
    constraint: AST.ImportConstraint


class ImportsManager:
    def __init__(self, project_name: str):
        self._project_name = project_name
        self._import_to_constraints: DefaultDict[AST.ReferenceImport, Set[StatementIdAndConstraint]] = defaultdict(set)

        self._postponed_annotations = False

        self._has_resolved_constraints = False
        self._has_written_top_imports = False

    def resolve_constraints(self, statements: Sequence[TopLevelStatement]) -> None:
        for statement in statements:
            for reference in statement.references:
                if reference.import_ is not None:
                    constraint = (
                        reference.import_.constraint
                        if reference.is_annotation
                        else AST.ImportConstraint.BEFORE_CURRENT_DECLARATION
                    )
                    if constraint is not None:
                        self._import_to_constraints[reference.import_].add(
                            StatementIdAndConstraint(
                                statement_id=statement.id,
                                constraint=constraint,
                            )
                        )

                        if reference.is_annotation and constraint == AST.ImportConstraint.AFTER_CURRENT_DECLARATION:
                            self._postponed_annotations = True

                    elif reference.import_ not in self._import_to_constraints:
                        # even if there's no constraints, we still store the import
                        # so that we write it to the file.
                        self._import_to_constraints[reference.import_] = set()

        self._has_resolved_constraints = True

    def write_top_imports_for_file(self, writer: AST.Writer) -> None:
        if not self._has_resolved_constraints:
            raise RuntimeError("Constraints haven't been resolved yet")
        if self._postponed_annotations:
            writer.write_line("from __future__ import annotations")
        self._has_written_top_imports = True

    def write_top_imports_for_statement(
        self, statement: TopLevelStatement, writer: AST.Writer, reference_resolver: ReferenceResolverImpl
    ) -> None:
        if not self._has_written_top_imports:
            raise RuntimeError("Top imports haven't been written yet")

        # write (and forget) all imports without any "after" constraints
        written_imports: Set[AST.ReferenceImport] = set()
        for import_, constraints in self._import_to_constraints.items():
            # if there's both a "before {this statement}" and "after {any statement}" constraint,
            # then the constraints are unresolvable
            must_be_before_this_statement = False
            must_be_after_statement: Optional[StatementId] = None
            for constraint in constraints:
                if constraint.constraint == AST.ImportConstraint.BEFORE_CURRENT_DECLARATION:
                    must_be_before_this_statement |= constraint.statement_id == statement.id
                elif constraint.constraint == AST.ImportConstraint.AFTER_CURRENT_DECLARATION:
                    must_be_after_statement = constraint.statement_id

            if must_be_after_statement is None:
                self._write_import(import_=import_, writer=writer, reference_resolver=reference_resolver)
                written_imports.add(import_)
            elif must_be_before_this_statement:
                raise RuntimeError(
                    f"Unresolvable constraint: import is constrained to be before {statement.id}"
                    + f" but after {must_be_after_statement}:"
                    + "\n\t"
                    + self._get_import_as_string(import_=import_, reference_resolver=reference_resolver)
                )
        for import_ in written_imports:
            del self._import_to_constraints[import_]

        # delete "must be after {statement} constraints"
        constraint_to_delete = StatementIdAndConstraint(
            statement_id=statement.id,
            constraint=AST.ImportConstraint.AFTER_CURRENT_DECLARATION,
        )
        for import_, constraints in self._import_to_constraints.items():
            if constraint_to_delete in constraints:
                constraints.remove(constraint_to_delete)

    def write_remaining_imports(self, writer: AST.Writer, reference_resolver: ReferenceResolverImpl) -> None:
        for import_ in self._import_to_constraints:
            self._write_import(import_=import_, writer=writer, reference_resolver=reference_resolver)

    def _write_import(
        self, import_: AST.ReferenceImport, writer: AST.Writer, reference_resolver: ReferenceResolverImpl
    ) -> None:
        writer.write_line(self._get_import_as_string(import_=import_, reference_resolver=reference_resolver))

    def _get_import_as_string(self, import_: AST.ReferenceImport, reference_resolver: ReferenceResolverImpl) -> str:
        resolved_import = reference_resolver.resolve_import(import_)
        module_str = ".".join(
            resolved_import.module.get_fully_qualfied_module_path(
                project_name=self._project_name,
            )
        )

        if resolved_import.named_import is None:
            s = f"import {module_str}"
        else:
            s = f"from {module_str} import {resolved_import.named_import}"
        if resolved_import.alias is not None:
            s += f" as {resolved_import.alias}"

        return s
