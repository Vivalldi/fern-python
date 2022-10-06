import typing

import pydantic
import typing_extensions


class FunctionImplementation(pydantic.BaseModel):
    impl: str
    imports: typing.Optional[str]

    @pydantic.validator("impl")
    def _validate_impl(cls, impl: str) -> str:
        for validator in FunctionImplementation.Validators._impl:
            impl = validator(impl)
        return impl

    @pydantic.validator("imports")
    def _validate_imports(cls, imports: typing.Optional[str]) -> typing.Optional[str]:
        for validator in FunctionImplementation.Validators._imports:
            imports = validator(imports)
        return imports

    class Validators:
        _impl: typing.ClassVar[str] = []
        _imports: typing.ClassVar[typing.Optional[str]] = []

        @typing.overload
        @classmethod
        def field(impl: typing_extensions.Literal["impl"]) -> str:
            ...

        @typing.overload
        @classmethod
        def field(imports: typing_extensions.Literal["imports"]) -> typing.Optional[str]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "impl":
                    cls._impl.append(validator)  # type: ignore
                elif field_name == "imports":
                    cls._imports.append(validator)  # type: ignore
                else:
                    raise RuntimeError("Field does not exist on FunctionImplementation: " + field_name)

                return validator

            return validator  # type: ignore

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True
