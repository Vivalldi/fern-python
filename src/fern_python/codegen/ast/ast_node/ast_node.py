from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Set

from ..reference import Reference
from .reference_resolver import ReferenceResolver


class AstNode(ABC):
    @abstractmethod
    def get_references(self) -> Set[Reference]:
        ...

    @abstractmethod
    def write(self, writer: Writer, reference_resolver: ReferenceResolver) -> None:
        ...


from .writer import Writer  # noqa: E402
