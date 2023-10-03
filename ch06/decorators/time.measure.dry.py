# decorators/time.measure.dry.py
from time import sleep, time


def f():
    sleep(.3)


def g():
    sleep(.5)


def measure(func):
    t = time()
    func()
    print(func.__name__, 'took:', time() - t)


measure(f)  # f took: 0.30434322357177734
measure(g)  # g took: 0.5048270225524902
