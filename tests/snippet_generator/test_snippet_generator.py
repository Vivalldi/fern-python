from fern_python.codegen import AST
from fern_python.source_file_factory import SourceFileFactory


def test_snippet_generator() -> None:
    snippet = SourceFileFactory.create_snippet()
    snippet.add_arbitrary_code(AST.CodeWriter("x = 42"))
    assert (
        snippet.to_str()
        == """# This file was auto-generated by Fern from our API Definition.

x = 42
"""
    )


"""
import Merge from merge.client
import MergeEnvironment from merge.environment

client = Merge(
  MergeEnvironment.Production,
)

"""

"""
GeneratedEnvironment: 
  environment_class_reference: AST.ClassReference
  example_environment: str

RootClientGenerator
  sync_instatition: str

ConstructorParameter: 
    value: AST.Expression

ConstructorParameter(
 = 
)
  
class RootClientInstantiationSnippet: 

    def __init__(self) -> None: 
        self.

    def generate(self, )-> None: 
    

        def write_client_instantiation(writer: AST.NodeWriter) -> 
            root_client_reference = AST.ClassRef(...)
            root_client_instantiation = AST.ClassInstatition(class_ref=root_client_reference, arguments=self.get_arguments())
            writer.write_node(AST.Expression(client_instantiation))
    
        snippet.add_arbitrary_code(AST.CodeWriter(write_client_instantiation))

        def get_arguments() -> List[AST.Expression]
            resulrt = []
            for param in self._constructor_params: 
                result.append(AST.Expfression(self.argument_codewriter()))
            
        
        def argument_codewriter(self, param_name: str, param_value: ) -> AST.CodeWriter: 
            def (writer: AST.NodeWriter) -> None:
                writer.write(f"{param_name}=")
                writer.write_node(AST.Expression(environment_reference))
                writer.write(".PRODUCTION")
                
            return writer
            
        
"""


def test_build_client_snippet() -> None:
    snippet = SourceFileFactory.create_snippet()

    def write_argument(writer: AST.NodeWriter) -> None:
        environment_reference = AST.ClassReference(
            qualified_name_excluding_import=(),
            import_=AST.ReferenceImport(
                module=AST.Module.local("merge.environment"),
                named_import="MergeEnvironment",
            ),
        )
        
        writer.write("environment=")
        writer.write_node(AST.Expression(environment_reference))
        writer.write(".PRODUCTION")

    def write_client_snippet(writer: AST.NodeWriter) -> None:
        client_class_reference = AST.ClassReference(
            qualified_name_excluding_import=(),
            import_=AST.ReferenceImport(
                module=AST.Module.local("merge.client"),
                named_import="Merge",
            ),
        )
        client_instantiation = AST.ClassInstantiation(
            class_=client_class_reference,
            args=[AST.Expression(AST.CodeWriter(write_argument))],
        )
        writer.write_node(AST.Expression(client_instantiation))
        writer.write_newline_if_last_line_not()

    snippet.add_arbitrary_code(AST.CodeWriter(write_client_snippet))

    print(snippet.to_str())

    assert False