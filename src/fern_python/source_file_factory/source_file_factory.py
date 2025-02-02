from __future__ import annotations

from typing import Set

from fern.generator_exec.resources import GeneratorUpdate, LogLevel, LogUpdate

from fern_python.codegen import Filepath, SourceFile
from fern_python.codegen.dependency_manager import DependencyManager
from fern_python.codegen.project import Project
from fern_python.codegen.reference_resolver_impl import ReferenceResolverImpl
from fern_python.codegen.source_file import SourceFileImpl
from fern_python.generator_exec_wrapper import GeneratorExecWrapper


class SourceFileFactory:
    @staticmethod
    def create(
        *,
        project: Project,
        filepath: Filepath,
        generator_exec_wrapper: GeneratorExecWrapper,
    ) -> SourceFile:
        SourceFileFactory._log_generating_file_update(
            filepath=filepath,
            generator_exec_wrapper=generator_exec_wrapper,
        )
        return project.source_file(filepath=filepath)

    @staticmethod
    def create_snippet() -> SourceFile:
        return SourceFileImpl(
            module_path=(),
            reference_resolver=ReferenceResolverImpl(
                module_path_of_source_file=(),
            ),
            dependency_manager=DependencyManager(),
            should_format=True,
            should_include_header=False,
        )

    @staticmethod
    def add_source_file_from_disk(
        *, project: Project, path_on_disk: str, filepath_in_project: Filepath, exports: Set[str]
    ) -> None:
        project.add_source_file_from_disk(
            path_on_disk=path_on_disk,
            filepath_in_project=filepath_in_project,
            exports=exports,
        )

    @staticmethod
    def _log_generating_file_update(*, filepath: Filepath, generator_exec_wrapper: GeneratorExecWrapper) -> None:
        generator_exec_wrapper.send_update(
            GeneratorUpdate.factory.log(LogUpdate(level=LogLevel.DEBUG, message=f"Generating {filepath}"))
        )
