import typing

import pydantic
import typing_extensions

from .function_implementation_for_multiple_languages import FunctionImplementationForMultipleLanguages
from .parameter import Parameter


class VoidFunctionDefinitionThatTakesActualResult(pydantic.BaseModel):
    additional_parameters: typing.List[Parameter] = pydantic.Field(alias="additionalParameters")
    code: FunctionImplementationForMultipleLanguages

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("additional_parameters")
    def _validate_additional_parameters(cls, additional_parameters: typing.List[Parameter]) -> typing.List[Parameter]:
        for validator in VoidFunctionDefinitionThatTakesActualResult.Validators._additional_parameters_validators:
            additional_parameters = validator(additional_parameters)
        return additional_parameters

    @pydantic.validator("code")
    def _validate_code(
        cls, code: FunctionImplementationForMultipleLanguages
    ) -> FunctionImplementationForMultipleLanguages:
        for validator in VoidFunctionDefinitionThatTakesActualResult.Validators._code_validators:
            code = validator(code)
        return code

    class Validators:
        _additional_parameters_validators: typing.ClassVar[
            typing.List[typing.Callable[[typing.List[Parameter]], typing.List[Parameter]]]
        ] = []
        _code_validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [FunctionImplementationForMultipleLanguages], FunctionImplementationForMultipleLanguages
                ]
            ]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["additional_parameters"]
        ) -> typing.Callable[
            [typing.Callable[[typing.List[Parameter]], typing.List[Parameter]]],
            typing.Callable[[typing.List[Parameter]], typing.List[Parameter]],
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["code"]
        ) -> typing.Callable[
            [typing.Callable[[FunctionImplementationForMultipleLanguages], FunctionImplementationForMultipleLanguages]],
            typing.Callable[[FunctionImplementationForMultipleLanguages], FunctionImplementationForMultipleLanguages],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "additional_parameters":
                    cls._additional_parameters_validators.append(validator)
                elif field_name == "code":
                    cls._code_validators.append(validator)
                else:
                    raise RuntimeError(
                        "Field does not exist on VoidFunctionDefinitionThatTakesActualResult: " + field_name
                    )

                return validator

            return decorator

    class Config:
        frozen = True
        allow_population_by_field_name = True
