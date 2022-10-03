import os
import shutil
import subprocess
from glob import glob
from pathlib import Path
from typing import List

from snapshottest.file import FileSnapshot  # type: ignore
from snapshottest.module import SnapshotTest  # type: ignore

from fern_python.cli import main as cli
from fern_python.generated import generator_exec


def test_pydantic_model(snapshot: SnapshotTest, tmpdir: Path) -> None:
    path_to_fixture = os.path.join(os.path.dirname(__file__), "fixtures/fern-ir")

    path_to_config_json = os.path.join(tmpdir, "config.json")
    path_to_output = os.path.join(tmpdir, "output/")
    path_to_ir = os.path.join(path_to_fixture, "ir.json")

    config = generator_exec.config.GeneratorConfig(
        ir_filepath=path_to_ir,
        output=generator_exec.config.GeneratorOutputConfig(path=path_to_output),
        workspace_name="ir",
        organization="fern",
        custom_config=None,
        environment=generator_exec.config.GeneratorEnvironment.local(),
    )

    with open(path_to_config_json, "w") as f:
        f.write(config.json(by_alias=True))

    symlink = Path(os.path.join(path_to_fixture, "generated"))
    if symlink.exists():
        if symlink.is_symlink():
            os.unlink(symlink)
        else:
            shutil.rmtree(symlink)
    os.mkdir(path_to_output)
    os.symlink(path_to_output, symlink)

    subprocess.run(
        ["fern", "ir", "--output", path_to_ir],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=path_to_fixture,
        check=True,
    )
    cli(path_to_config_json)

    # snapshot files
    written_filepaths = glob(os.path.join(path_to_output, "**/*.py"), recursive=True)
    relative_filepaths: List[str] = []
    for written_filepath in written_filepaths:
        relative_filepath = os.path.relpath(written_filepath, start=path_to_output)
        relative_filepaths.append(relative_filepath)
        snapshot.assert_match(
            name=relative_filepath.replace("/", "_").replace(".py", ""), value=FileSnapshot(written_filepath)
        )
    snapshot.assert_match(
        name="filepaths",
        value=relative_filepaths,
    )
