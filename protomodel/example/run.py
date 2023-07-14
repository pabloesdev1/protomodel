import importlib.util
from protomodel import message, service
from typing import TextIO, List

input_filename = "hello.py"
output_filename = "data.proto"
package_name = "app.proto"

data_spec = importlib.util.spec_from_file_location(input_filename.split(".")[0], input_filename)
data_module = importlib.util.module_from_spec(data_spec)
data_spec.loader.exec_module(data_module)

proto_file: TextIO = open(f"./{output_filename}", "w")
proto_file.write(f'syntax = "proto3";\n\npackage {package_name};\n\n')

messages: List[message] = [cls for cls in data_module.__dict__.values() if isinstance(cls, message)]
services: List[service] = [cls for cls in data_module.__dict__.values() if isinstance(cls, service)]

for msg in messages:
    msg.add_field(proto_file)

for service in services:
    service.add_field(proto_file)

print('file created.')
proto_file.close()