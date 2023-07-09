from typing import Any, Dict, List, TextIO, Type
from protomodel.types import get_types


class Message:

    """A decorator class to define a proto buffer model"""

    def __init__(self, message_model: Type[Any]):
        self.message_model = message_model

    def __call__(self, *args: Any, **kwds: Dict[str, Any]) -> Dict[str, Any]:
        return self.message_model.__annotations__

    def add_field(self, file: TextIO) -> None:
        file.write(f"{self.__class__.__name__.lower()} {self.message_model.__name__} {{\n")
        annotations = self.message_model.__annotations__

        for index, field in enumerate(annotations, 1):
            annotation: Type[Any] = annotations[field]
            field_type: str = self.__get_type_string(annotation)
            file.write(f"\t{field_type} {field} = {index};\n")

        file.write(f"}}\n\n")

    def __get_type_string(self, annotation: Type[Any]) -> str:
        if hasattr(annotation, "__origin__") and annotation.__origin__ in [List, list]:
            return f"{get_types(annotation.__name__)} {annotation.__args__[0].message_model.__name__}"
        try:
            return get_types(annotation.__name__)
        except:
            return annotation.message_model.__name__ if hasattr(annotation, "message_model") else annotation.__name__