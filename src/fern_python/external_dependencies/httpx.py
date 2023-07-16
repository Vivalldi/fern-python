from typing import List, Optional, Tuple

from fern_python.codegen import AST

HTTPX_MODULE = AST.Module.external(
    module_path=("httpx",),
    dependency=AST.Dependency(
        name="httpx",
        version="0.23.3",
    ),
)


class HttpX:
    _ASYNC_CLIENT_NAME = "_client"

    ASYNC_CLIENT = AST.ClassReference(
        qualified_name_excluding_import=("AsyncClient",),
        import_=AST.ReferenceImport(module=HTTPX_MODULE),
    )

    CLIENT = AST.ClassReference(
        qualified_name_excluding_import=("Client",),
        import_=AST.ReferenceImport(module=HTTPX_MODULE),
    )

    BASIC_AUTH = AST.ClassReference(
        qualified_name_excluding_import=("BasicAuth",),
        import_=AST.ReferenceImport(module=HTTPX_MODULE),
    )

    @staticmethod
    def make_request(
        *,
        url: AST.Expression,
        method: str,
        query_parameters: List[Tuple[str, str, bool, AST.Expression]],
        request_body: Optional[AST.Expression],
        headers: Optional[AST.Expression],
        files: Optional[AST.Expression],
        auth: Optional[AST.Expression],
        timeout: AST.Expression,
        response_variable_name: str,
        is_async: bool,
        is_streaming: bool,
        response_code_writer: AST.CodeWriter,
        reference_to_client: AST.Expression,
    ) -> AST.Expression:
        def add_request_params(*, writer: AST.NodeWriter) -> None:
            if len(query_parameters) > 0:
                writer.write("params=params")
                writer.write_line(",")

            if request_body is not None:
                writer.write("data=" if files is not None else "json=")
                writer.write_node(request_body)
                writer.write_line(",")

            if files is not None:
                writer.write("files=")
                writer.write_node(files)
                writer.write_line(",")

            if headers is not None:
                writer.write("headers=")
                writer.write_node(headers)
                writer.write_line(",")

            if auth is not None:
                writer.write("auth=")
                writer.write_node(auth)
                writer.write_line(",")

            writer.write("timeout=")
            writer.write_node(timeout)

        def add_query_params(*, writer: AST.NodeWriter) -> None:
            if len(query_parameters) == 0:
                return
            writer.write_line("params={")
            for i, (query_parameter_key, query_parameter_name, query_parameter_is_optional, query_parameter_value) in enumerate(query_parameters):
                if i > 0:
                    writer.write_line(", ")
                writer.write(f'"{query_parameter_key}": ')
                writer.write_node(query_parameter_value)
            writer.write_line()
            writer.write_line("}")

            for i, (query_parameter_key, query_parameter_name, query_parameter_is_optional, query_parameter_value) in enumerate(query_parameters):
                if query_parameter_is_optional:
                    writer.write(f'if {query_parameter_name} is None:')
                    writer.write_line()
                    with writer.indent():
                        writer.write(f'del params["{query_parameter_key}"]')
                        writer.write_line()

        def write_non_streaming_call(
            *,
            writer: AST.NodeWriter,
        ) -> None:
            make_non_streaming_request(writer=writer)
            response_code_writer.write(writer=writer)

        def make_non_streaming_request(
            *,
            writer: AST.NodeWriter,
        ) -> None:

            add_query_params(writer=writer)
            writer.write(f"{response_variable_name} = ")
            if is_async:
                writer.write("await ")
            writer.write_node(reference_to_client)
            writer.write(f'.request("{method}", ')
            writer.write_node(url)
            writer.write(", ")
            with writer.indent():
                add_request_params(writer=writer)
            writer.write_line(")")

        def write_streaming_call(*, writer: AST.NodeWriter) -> None:
            add_query_params(writer=writer)
            if is_async:
                writer.write("async ")
            writer.write("with ")
            writer.write_node(reference_to_client)
            writer.write(f'.stream("{method}", ')
            writer.write_node(url)
            writer.write(", ")
            with writer.indent():
                add_request_params(writer=writer)
            writer.write_line(f") as {response_variable_name}:")

            with writer.indent():
                response_code_writer.write(writer=writer)

        def write(writer: AST.NodeWriter) -> None:
            if is_async:
                if is_streaming:
                    write_streaming_call(
                        writer=writer,
                    )
                else:
                    write_non_streaming_call(
                        writer=writer,
                    )
            else:
                if is_streaming:
                    write_streaming_call(
                        writer=writer,
                    )
                else:
                    write_non_streaming_call(
                        writer=writer,
                    )

        return AST.Expression(AST.CodeWriter(write))
