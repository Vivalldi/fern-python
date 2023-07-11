import os
import shutil
import subprocess
from glob import glob
from pathlib import Path
from typing import Any, Callable, List, Optional, Set, Union

from fern.generator_exec.resources import config
from snapshottest.file import FileSnapshot  # type: ignore
from snapshottest.module import SnapshotTest  # type: ignore

PYTHON_VERSION = "3.8.16"


def run_snapshot_test(
    *,
    filename_of_test: str,
    fixture_name: str,
    snapshot: SnapshotTest,
    tmpdir: Path,
    cli: Callable[[str], None],
    custom_config: Any = None,
    output_mode: config.OutputMode = config.OutputMode.factory.download_files(),
    test_commands: Optional[List[str]] = None,
    organization: str = "fern",
) -> None:
    path_to_fixture = os.path.join(os.path.dirname(filename_of_test), f"fixtures/{fixture_name}")

    path_to_config_json = os.path.join(tmpdir, "config.json")
    path_to_output = os.path.join(tmpdir, "output/")
    path_to_ir = os.path.join(path_to_fixture, "ir.json")

    generator_config = config.GeneratorConfig(
        ir_filepath=path_to_ir,
        output=config.GeneratorOutputConfig(path=path_to_output, mode=output_mode),
        workspace_name="ir",
        organization=organization,
        custom_config=custom_config,
        environment=config.GeneratorEnvironment.factory.local(),
        dry_run=True,
    )

    with open(path_to_config_json, "w") as f:
        f.write(generator_config.json(by_alias=True))

    os.mkdir(path_to_output)

    symlink = Path(os.path.join(path_to_fixture, "generated"))
    if symlink.is_symlink():
        os.unlink(symlink)
    elif symlink.is_file():
        os.remove(symlink)
    elif symlink.is_dir():
        shutil.rmtree(symlink)
    elif symlink.exists():
        raise RuntimeError(f"Cannot delete {symlink}")
    os.symlink(path_to_output, symlink)

    subprocess.run(
        ["npx", "--yes", "fern-api", "ir", path_to_ir, "--language", "python"],
        cwd=path_to_fixture,
        check=True,
    )
    cli(path_to_config_json)

    # snapshot files
    written_filepaths = glob(os.path.join(path_to_output, "**/*.py"), recursive=True)
    relative_filepaths: Set[str] = set()
    for written_filepath in written_filepaths:
        relative_filepath = os.path.relpath(written_filepath, start=path_to_output)
        relative_filepaths.add(relative_filepath)
        snapshot.assert_match(
            name=relative_filepath.replace("/", "_").replace(".py", ""), value=FileSnapshot(written_filepath)
        )

    snapshot.assert_match(
        name="filepaths",
        value=sorted(list(relative_filepaths)),
    )

    # check compile
    def run_command_in_output_directory(command: Union[str, List[str]], shell: bool = False) -> None:
        print("+ " + command if type(command) is str else " ".join(command))
        proc = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=path_to_output, text=True, shell=shell
        )
        print(f"Return code: {proc.returncode}")
        print(proc.stdout)
        proc.check_returncode()

    if output_mode.get_as_union().type == "downloadFiles":
        run_command_in_output_directory(["poetry", "init", "--no-interaction", "--python", PYTHON_VERSION])
        run_command_in_output_directory(["poetry", "env", "use", PYTHON_VERSION])
        run_command_in_output_directory(
            [
                "poetry",
                "add",
                "fastapi=0.92.0",
                "pydantic=1.10.5",
                "mypy=1.0.1",
                "httpx=0.23.3",
                "backports.cached_property=1.0.2",
                "types-backports=0.1.3",
            ]
        )

    if test_commands is not None:
        for command in test_commands:
            run_command_in_output_directory(command, shell=True)
