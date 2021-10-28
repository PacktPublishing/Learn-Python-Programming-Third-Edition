# exceptions/trace.back.py
def squareroot(number):
    if number < 0:
        raise ValueError("No negative numbers please")
    return number ** .5

def quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    return ((-b - squareroot(d)) / (2 * a),
            (-b + squareroot(d)) / (2 * a))

quadratic(1, 0, 1)  # x**2 + 1 == 0


"""
$ python exceptions/trace.back.py
Traceback (most recent call last):
  File "exceptions/trace.back.py", line 12, in <module>
    quadratic(1, 0, 1)  # x**2 + 1 == 0
  File "exceptions/trace.back.py", line 9, in quadratic
    return ((-b - squareroot(d)) / (2 * a),
  File "exceptions/trace.back.py", line 4, in squareroot
    raise ValueError("No negative numbers please")
ValueError: No negative numbers please
"""
