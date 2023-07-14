from typing import Any, Dict, List, TextIO, Type
from protomodel.rpc import RPC
from protomodel import rpc
from protomodel.types import get_types
import inspect

class Service:

    """A decorator class to define a proto buffer model"""

    def __init__(self, service_model: Type[Any]):
        self.service_model = service_model

    def __call__(self, *args: Any, **kwds: Dict[str, Any]) -> Dict[str, Any]:
        print(self.service_model.__annotations__)
        return self.service_model.__annotations__

    def add_field(self, file: TextIO):
        file.write(f"{self.__class__.__name__.lower()} {self.service_model.__name__} {{\n")
        rpc_list: list[type[rpc]] = [o for m, o in inspect.getmembers(self.service_model) if isinstance(o, RPC)]
        
        for rpc_method in rpc_list:
            temp_name = rpc_method.rpc_model.__name__.split('_')
            rpc_method_name = ''.join(ele.title() for ele in temp_name[0:])
            params_list = []
            return_type = None
            rpc_annotations: dict[str, Any] =  rpc_method.rpc_model.__annotations__

            for item in rpc_annotations:
                ann: Type[Any] = rpc_annotations[item]
                field_type: str = self.__get_type_string(ann)
                if item == 'return':
                    return_type = field_type
                else:
                    params_list.append(field_type)
            params_list = '' if len(params_list) == 0 else params_list[0]
            file.write(f"  {rpc_method.__class__.__name__.lower()} {rpc_method_name} ({params_list}) returns ({return_type}) {{}}\n")
        file.write(f"}}\n\n")


    def __get_type_string(self, annotation: Type[Any]) -> str:
        if hasattr(annotation, "__origin__") and annotation.__origin__ in [List, list]:
            return f"{get_types(annotation.__name__)} {annotation.__args__[0].message_model.__name__}"
        try:
            return get_types(annotation.__name__)
        except:
            return annotation.message_model.__name__ if hasattr(annotation, "message_model") else annotation.__name__