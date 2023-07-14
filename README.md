

# Protomodel
Python Library to generate proto buffer code from python using type hints

## Example
Generate a file hello.py and add the following code:
```python
from protomodel import message, service, rpc


@message
class HelloRequest:
    name: str

@message
class HelloReply:
    message: str

@service
class Greeter:

    @rpc
    def say_hello(hello_request: HelloRequest) -> HelloReply:
        ...

```

## Generate file

Run the following command to generate a proto buffer file
```bash
python -m protomodel generate --python_file=hello.py --proto_name=hello.proto
```


And then you will get the following result:
```proto
syntax = "proto3";

package app.proto;

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}

service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}
```