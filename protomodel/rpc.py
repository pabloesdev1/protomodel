from typing import Any, Dict, Type


class RPC:

    """A decorator class to define a rpc model"""

    def __init__(self, rpc_model: Type[Any]):
        self.rpc_model = rpc_model

    def __call__(self, *args: Any, **kwds: Dict[str, Any]) -> Dict[str, Any]:
        print(self.rpc_model.__annotations__)
        return self.rpc_model.__annotations__
