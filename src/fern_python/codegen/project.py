from __future__ import annotations

import concurrent.futures
import os
from dataclasses import dataclass
from glob import glob
from pathlib import Path
from types import TracebackType
from typing import Optional, Set, Type

import black

from fern_python.codegen.pyproject_toml import PyProjectToml, PyProjectTomlPackageConfig

from .dependency_manager import DependencyManager
from .filepath import Filepath
from .module_manager import ModuleManager
from .reference_resolver_impl import ReferenceResolverImpl
from .source_file import SourceFile, SourceFileImpl
from .writer_impl import WriterImpl


@dataclass(frozen=True)
class PublishConfig:
    package_name: str
    package_version: str


class Project:
    """
    with Project("/path/to/project") as project:
        ...
    """

    def __init__(
        self,
        filepath: str,
        project_name: str,
        python_version: str = "3.7",
        publish_config: PublishConfig = None,
        generate_py_typed: bool = False,
    ) -> None:
        self._project_filepath = filepath if publish_config is None else os.path.join(filepath, "src", project_name)
        self._root_filepath = filepath
        self._project_name = project_name
        self._publish_config = publish_config
        self._module_manager = ModuleManager()
        self._python_version = python_version
        self._dependency_manager = DependencyManager()
        self._generate_py_typed = generate_py_typed

    def source_file(self, filepath: Filepath) -> SourceFile:
        """
        with project.source_file() as source_file:
            ...
        """

        def on_finish(source_file: SourceFileImpl) -> None:
            self._module_manager.register_exports(
                filepath=filepath,
                exports=source_file.get_exports(),
            )

        module = filepath.to_module()
        source_file = SourceFileImpl(
            filepath=self._get_source_file_filepath(filepath),
            module_path=module.path,
            completion_listener=on_finish,
            reference_resolver=ReferenceResolverImpl(
                module_path_of_source_file=module.path,
            ),
            dependency_manager=self._dependency_manager,
        )
        return source_file

    def _get_source_file_filepath(self, filepath: Filepath) -> str:
        return os.path.join(self._project_filepath, str(filepath))

    def add_source_file_from_disk(self, *, path_on_disk: str, filepath_in_project: Filepath, exports: Set[str]) -> None:
        with open(path_on_disk, "r") as existing_file:
            with WriterImpl(self._get_source_file_filepath(filepath_in_project)) as writer:
                writer.write(existing_file.read())
        self._module_manager.register_exports(
            filepath=filepath_in_project,
            exports=exports,
        )

    def finish(self) -> None:
        self._module_manager.write_modules(filepath=self._project_filepath)

        with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count() or 1) as executor:
            results = [
                executor.submit(_format_file, Path(path))
                for path in glob(os.path.join(self._project_filepath, "**/*.py"), recursive=True)
            ]
            concurrent.futures.wait(results)

        if self._publish_config is not None:
            # generate pyproject.toml
            py_project_toml = PyProjectToml(
                name=self._publish_config.package_name,
                version=self._publish_config.package_version,
                package=PyProjectTomlPackageConfig(include=self._project_name, _from="src"),
                path=self._root_filepath,
                dependency_manager=self._dependency_manager,
                python_version=self._python_version,
            )
            py_project_toml.write()
            # generate py.typed
            with open(os.path.join(self._project_filepath, "py.typed"), "w") as f:
                f.write("")

    def __enter__(self) -> Project:
        return self

    def __exit__(
        self,
        exctype: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ) -> None:
        self.finish()


def _format_file(path: Path) -> None:
    print(f"Formatting {path}")
    black.format_file_in_place(
        src=path,
        fast=True,
        # todo read their config?
        mode=black.FileMode(magic_trailing_comma=False, line_length=120),
        write_back=black.WriteBack.YES,
    )
