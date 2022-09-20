import pydantic

from ...commons.with_docs import WithDocs
from ..commons.declared_service_name import DeclaredServiceName
from .web_socket_messenger import WebSocketMessenger
from .web_socket_operation_properties import WebSocketOperationProperties


class WebSocketChannel(WithDocs):
    name: DeclaredServiceName
    path: int
    client: WebSocketMessenger
    server: WebSocketMessenger
    operation_properties: WebSocketOperationProperties = pydantic.Field(alias="operationProperties")

    class Config:
        allow_population_by_field_name = True
