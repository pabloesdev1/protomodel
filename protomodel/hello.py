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