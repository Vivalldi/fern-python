

from fern_python.codegen import AST
from fern_python.codegen.dependency_manager import DependencyManager
from fern_python.codegen.filepath import Filepath
from fern_python.codegen.reference_resolver_impl import ReferenceResolverImpl
from fern_python.codegen.source_file import InMemorySourceFileImpl, SourceFileImpl


class SnippetGenerator:

    def __init__(self) -> None:
        self._source_file = InMemorySourceFileImpl(
            reference_resolver=ReferenceResolverImpl(
                module_path_of_source_file=(),
            ),
            dependency_manager=DependencyManager(),
        )
        
    def add_code(self, code: AST.CodeWriter) -> None:
        self._source_file.add_arbitrary_code(code)
    
    def generate(self) -> str: 
        return self._source_file.finish()
    