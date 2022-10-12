from fern_python.codegen import AST

STARLETTE_MODULE = AST.Module.external(
    module_path=("starlette",),
    dependency=AST.Dependency(
        name="starlette",
        version="^0.21.0",
    ),
)


def _export(*name: str) -> AST.ClassReference:
    return AST.ClassReference(
        qualified_name_excluding_import=name, import_=AST.ReferenceImport(module=STARLETTE_MODULE)
    )


class Starlette:
    HTTPException = _export("HTTPException")

    HTTPException_STATUS_CODE_MEMBER = "status_code"
    HTTPException_DETAIL_MEMBER = "detail"
