from dataclasses import dataclass

from fern_python.codegen import AST


@dataclass
class GeneratedEnvironment:
    class_reference: AST.ClassReference
    environment_enum: str
