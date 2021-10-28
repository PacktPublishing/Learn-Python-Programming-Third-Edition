# json_examples/json_cplx.py
import json


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        print(f"ComplexEncoder.default: {obj=}")
        if isinstance(obj, complex):
            return {
                '_meta': '_complex',
                'num': [obj.real, obj.imag],
            }
        return super().default(obj)


data = {
    'an_int': 42,
    'a_float': 3.14159265,
    'a_complex': 3 + 4j,
}

json_data = json.dumps(data, cls=ComplexEncoder)

print(json_data)


def object_hook(obj):
    print(f"object_hook: {obj=}")
    try:
        if obj['_meta'] == '_complex':
            return complex(*obj['num'])
    except KeyError:
        return obj


data_out = json.loads(json_data, object_hook=object_hook)
print(data_out)
