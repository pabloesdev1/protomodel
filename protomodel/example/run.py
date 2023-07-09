import data
from protomodel import message, service, rpc
from typing import TextIO, List, Type, Any

input_filename = "data.py"
output_filename = "data.proto"
    
proto_file: TextIO = open(f"./{output_filename}", "w")
proto_file.write('syntax = "proto3";\n\npackage app.proto;\n\n')

# global_symbols = globals()
# messages = [cls for cls in global_symbols.values() if isinstance(cls, message)]
messages: List[message] = [cls for cls in data.__dict__.values() if isinstance(cls, message)]

for msg in messages:
    msg.add_field(proto_file)

print('file created.')
proto_file.close()