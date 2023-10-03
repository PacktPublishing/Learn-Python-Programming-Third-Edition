# oop/class.attribute.shadowing.py
class Point:
    x = 10
    y = 7


p = Point()
print(p.x)  # 10 (from class attribute)
print(p.y)  # 7 (from class attribute)

p.x = 12  # p gets its own `x` attribute
print(p.x)  # 12 (now found on the instance)
print(Point.x)  # 10 (class attribute still the same)

del p.x  # we delete instance attribute
print(p.x)  # 10 (now search has to go again to find class attr)

p.z = 3  # let's make it a 3D point
print(p.z)  # 3

print(Point.z)
# AttributeError: type object 'Point' has no attribute 'z'


"""
$ python class.attribute.shadowing.py
10
7
12
10
10
3
Traceback (most recent call last):
  File "/Users/fab/srv/lpp3e/v3/ch06/oop/class.attribute.shadowing.py", 
  line 20, in <module>
    print(Point.z)
AttributeError: type object 'Point' has no attribute 'z'
"""
