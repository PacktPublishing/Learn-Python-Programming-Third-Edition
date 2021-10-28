# json_examples/json_basic.py
import sys
import json


data = {
    'big_number': 2 ** 3141,
    'max_float': sys.float_info.max,
    'a_list': [2, 3, 5, 7],
}


json_data = json.dumps(data)
data_out = json.loads(json_data)

assert data == data_out  # json and back, data matches


# let's see how passing indent affects dumps.

info = {
    'full_name': 'Sherlock Holmes',
    'address': {
        'street': '221B Baker St',
        'zip': 'NW1 6XE',
        'city': 'London',
        'country': 'UK',
    }
}


print(json.dumps(info, indent=2, sort_keys=True))
