# json_examples/json_datetime.py
# exercise: do the same for date
import json
from datetime import datetime, timedelta, timezone


now = datetime.now()
now_tz = datetime.now(tz=timezone(timedelta(hours=1)))


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            try:
                off = obj.utcoffset().seconds
            except AttributeError:
                off = None

            return {
                '_meta': '_datetime',
                'data': obj.timetuple()[:6] + (obj.microsecond, ),
                'utcoffset': off,
            }
        return super().default(obj)


data = {
    'an_int': 42,
    'a_float': 3.14159265,
    'a_datetime': now,
    'a_datetime_tz': now_tz,
}

json_data = json.dumps(data, cls=DatetimeEncoder)

print(json_data)


def object_hook(obj):
    try:
        if obj['_meta'] == '_datetime':
            if obj['utcoffset'] is None:
                tz = None
            else:
                tz = timezone(timedelta(seconds=obj['utcoffset']))
            return datetime(*obj['data'], tzinfo=tz)
    except KeyError:
        return obj


data_out = json.loads(json_data, object_hook=object_hook)
from pprint import pprint
pprint(data_out, indent=2)
print(data_out)

assert data_out['a_datetime'] == data['a_datetime']
assert data_out['a_datetime_tz'] == data['a_datetime_tz']
