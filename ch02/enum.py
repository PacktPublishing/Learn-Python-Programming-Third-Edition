GREEN = 1
YELLOW = 2
RED = 4
TRAFFIC_LIGHTS = (GREEN, YELLOW, RED)

# or with a dict
traffic_lights = {'GREEN': 1, 'YELLOW': 2, 'RED': 4}

# using enum
from enum import Enum
class TrafficLight(Enum):
    GREEN = 1
    YELLOW = 2
    RED = 4

print(TrafficLight.GREEN)
print(TrafficLight.GREEN.name)

print(TrafficLight.GREEN.value)
print(TrafficLight(1))
print(TrafficLight(4))