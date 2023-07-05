from typing import Any, List, Type
from protomodel.types import get_types


class Message:


    def __init__(self, message: Type[Any]):
        self.message = message

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.message.__annotations__

    def add_messages(self, file) -> None:
        file.write(f"message {self.message.__name__} {{\n")

        for index, field in enumerate(self.message.__annotations__, 1):
            original_type = self.message.__annotations__[field]
            type_field = self.get_type_string(original_type)
            file.write(f"\t{type_field} {field} = {index};\n")

        file.write(f"}}\n\n")

    def get_type_string(self, type_hint):
        if hasattr(type_hint, "__origin__") and type_hint.__origin__ in [List, list]:
            return f"{get_types(type_hint.__name__)} {type_hint.__args__[0].message.__name__}"
        else:
            return get_types(type_hint.__name__)