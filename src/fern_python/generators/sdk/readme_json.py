import os
from typing import Optional

import fern.ir.resources as ir_types
from fern.generator_exec import Readme

from fern_python.codegen import AST


class ReadmeJson:
    def __init__(
        self,
        *,
        registry_url: Optional[str],
        package_name: str,
        root_client_class_name: str,
        root_client_module: AST.Module,
        path: str,
        auth: ir_types.ApiAuth,
    ):
        self._registry_url = registry_url
        self._package_name = package_name
        self._root_client_module = root_client_module
        self._root_client_class_name = root_client_class_name
        self._path = path
        self._auth = auth

    def write(self) -> None:
        readme = Readme(
            title=self._title(self._root_client_class_name),
            summary=self._summary(self._root_client_class_name),
            badges=self._badge(self._registry_url, self._package_name),
            installation=self._installation(self._registry_url, self._package_name),
            instantiation=self._instantiation(self._root_client_class_name, self._root_client_module, self._auth),
            usage="",
            status=self._status(),
        )
        with open(os.path.join(self._path, "readme.json"), "w") as f:
            f.write(readme.json())

    def _title(self, root_client_class_name: str) -> str:
        return f"# {root_client_class_name} Python Library"

    def _badge(self, registry_url: Optional[str], package_name: str) -> str:
        if registry_url is None:
            # A badge only makes sense if the package is available on PyPi.
            return ""
        formatted_registry_url = registry_url.rstrip("/")
        return f"[![pypi](https://img.shields.io/pypi/v/{package_name}.svg)](https://{formatted_registry_url}/pypi/{package_name})"

    def _summary(self, root_client_class_name: str) -> str:
        return f"The {root_client_class_name} Python library provides access to the {root_client_class_name} API from Python."

    def _installation(self, registry_url: Optional[str], package_name: str) -> str:
        if registry_url is None:
            # An installation guide only makes sense if the package is available on PyPi.
            return ""

        return f"""```sh
pip install --upgrade {package_name}"
```"""

    def _instantiation(
        self, root_client_class_name: str, root_client_module: AST.Module, auth: ir_types.ApiAuth
    ) -> str:
        parameters = ""
        if len(auth.schemes) > 0:
            parameters = auth.schemes[0].visit(
                bearer=self._get_auth_bearer_client_option,
                basic=self._get_auth_basic_client_option,
                header=self._get_auth_header_client_option,
            )
        module_path = ".".join(root_client_module.path)
        return f"""```pythoutn
from {module_path} import {root_client_class_name}

client = {root_client_class_name}({parameters})
```"""

    def _get_auth_bearer_client_option(self, bearer: ir_types.BearerAuthScheme) -> str:
        return f'{bearer.token.snake_case.safe_name}=<"YOUR_{bearer.token.screaming_snake_case.safe_name}">'

    def _get_auth_basic_client_option(self, basic: ir_types.BasicAuthScheme) -> str:
        return f'{basic.username.snake_case.safe_name}=<"YOUR_{basic.username.screaming_snake_case.safe_name}">, {basic.password.snake_case.safe_name}=<"YOUR_{basic.password.screaming_snake_case.safe_name}">'

    def _get_auth_header_client_option(self, header: ir_types.HeaderAuthScheme) -> str:
        return f'{header.name.name.snake_case.safe_name}=<"YOUR_{header.name.name.screaming_snake_case.safe_name}">'

    def _status(self) -> str:
        return """This SDK is in beta, and there may be breaking changes between versions without a major version update.
Therefore, we recommend pinning the package version to a specific version in your `pyproject.toml` file. This way,
you can install the same version each time without breaking changes unless you are intentionally looking for the
latest version.
"""
