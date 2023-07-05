def get_types(value):
    types = {
        "int": "int32",
        "str": "string",
        "list": "repetead",
        "List": 'repetead'
    }
    return types[value]