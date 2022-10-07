import os
import shutil
import subprocess
from glob import glob
from pathlib import Path
from typing import Callable, Set

from generator_exec.resources import config
from snapshottest.file import FileSnapshot  # type: ignore
from snapshottest.module import SnapshotTest  # type: ignore


def run_snapshot_test(
    *,
    filename_of_test: str,
    snapshot: SnapshotTest,
    tmpdir: Path,
    cli: Callable[[str], None],
) -> None:
    path_to_fixture = os.path.join(os.path.dirname(filename_of_test), "fixtures/fern-ir")

    path_to_config_json = os.path.join(tmpdir, "config.json")
    path_to_output = os.path.join(tmpdir, "output/")
    path_to_ir = os.path.join(path_to_fixture, "ir.json")

    generator_config = config.GeneratorConfig(
        ir_filepath=path_to_ir,
        output=config.GeneratorOutputConfig(
            path=path_to_output,
            mode=config.OutputMode.factory.publish(
                config.GeneratorPublishConfig(
                    registries=config.GeneratorRegistriesConfig(
                        maven=config.MavenRegistryConfig(registry_url="", username="", password="", group=""),
                        npm=config.NpmRegistryConfig(registry_url="", token="", scope=""),
                    ),
                    registries_v_2=config.GeneratorRegistriesConfigV2(
                        maven=config.MavenRegistryConfigV2(registry_url="", username="", password="", coordinate=""),
                        npm=config.NpmRegistryConfigV2(registry_url="", token="", package_name=""),
                        pypi=config.PypiRegistryConfig(registry_url="", username="", password="", package_name=""),
                    ),
                    version="0.0.0",
                )
            ),
        ),
        workspace_name="ir",
        organization="fern",
        custom_config=None,
        environment=config.GeneratorEnvironment.factory.local(),
    )

    with open(path_to_config_json, "w") as f:
        f.write(generator_config.json(by_alias=True))

    symlink = Path(os.path.join(path_to_fixture, "generated"))
    if symlink.exists():
        if symlink.is_symlink():
            os.unlink(symlink)
        else:
            shutil.rmtree(symlink)
    os.mkdir(path_to_output)
    os.symlink(path_to_output, symlink)

    subprocess.run(
        ["npx", "fern-api@0.0.207", "ir", "--output", path_to_ir],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
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
        value=relative_filepaths,
    )
