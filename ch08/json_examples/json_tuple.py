# json_examples/json_tuple.py
import json


data_in = {
    'a_tuple': (1, 2, 3, 4, 5),
}


json_data = json.dumps(data_in)
print(json_data)  # {"a_tuple": [1, 2, 3, 4, 5]}
data_out = json.loads(json_data)
print(data_out)  # {'a_tuple': [1, 2, 3, 4, 5]}
