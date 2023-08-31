from fern_python.codegen import Filepath

from .sdk_declaration_referencer import SdkDeclarationReferencer


class EnvironmentsEnumDeclarationReferencer(SdkDeclarationReferencer[None]):
    ENVIRONMENTS_FILEPATH = Filepath(
        directories=(),
        file=Filepath.FilepathPart(module_name="environment"),
    )

    def __init__(self, client_class_name: str):
        super().__init__()
        self._client_class_name = client_class_name

    def get_filepath(self, *, name: None) -> Filepath:
        return EnvironmentsEnumDeclarationReferencer.ENVIRONMENTS_FILEPATH

    def get_class_name(self, *, name: None) -> str:
        return self._client_class_name + "Environment"
