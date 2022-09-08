import pydantic
import typer

from fern_python.codegen import AST, Project, Filepath, ExportStrategy
from fern_python.ir_types import (
    AliasTypeDeclaration,
    ContainerType,
    IntermediateRepresentation,
    MapType,
    Type,
    TypeReference,
)


def main(path_to_config_json: str) -> None:
    print(f"Path to config: {path_to_config_json}")
    map = TypeReference.container(
        ContainerType.map(MapType(key_type=TypeReference.void(), value_type=TypeReference.void()))
    )

    processTypeReference(map)

    optional = TypeReference.container(ContainerType.optional(TypeReference.void()))
    processTypeReference(optional)
    print(optional.json(by_alias=True))

    type = Type.alias(AliasTypeDeclaration(alias_of=map))
    print(type.json(by_alias=True))

    print(map.json(by_alias=True))

    parsedContainer = TypeReference.parse_raw(
        """
    {
        "type": "container",
        "container": {
            "type": "map",
            "keyType": {
                "type": "void"
            },
            "valueType": {
                "type": "void"
            }
        }
    }
    """
    )
    print(parsedContainer.json(by_alias=True))

    parsed = pydantic.parse_file_as(IntermediateRepresentation, "ir.json")
    with open("parsed_ir.json", "w") as f:
        f.write(parsed.json(by_alias=True))

    with Project(filepath="./foo") as project:
        with project.source_file(
            filepath=Filepath(
                directories=[
                    Filepath.DirectoryFilepathPart(module_name="bar", export_strategy=ExportStrategy.EXPORT_ALL)
                ],
                file=Filepath.FilepathPart(module_name="baz"),
            )
        ) as source_file:
            class_declaration = source_file.add_class(class_name="ZachClass")
            class_declaration.add_variable(AST.VariableDeclaration(name="foo"))


def processTypeReference(x: TypeReference) -> None:
    pass


if __name__ == "__main__":
    typer.run(main)
