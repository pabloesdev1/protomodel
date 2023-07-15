def get_types(value):
    types = {
        "int": "int32",
        "str": "string",
        "float": "double",
        "bool": "bool",
        "bytes": "bytes",
        "list": "repeated",
        "List": 'repeated',
    }
    return types[value]
