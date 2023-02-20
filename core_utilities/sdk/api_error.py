import typing


class ApiError:
    status_code: typing.Optional[int]
    body: typing.Any

    def __init__(self, *, status_code: typing.Optional[int] = None, body: typing.Any = None):
        self.status_code = status_code
        self.body = body
