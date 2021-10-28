# oop/multiple.inheritance.py
class Shape:
    geometric_type = 'Generic Shape'

    def area(self):  # This acts as placeholder for the interface
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type


class Plotter:

    def plot(self, ratio, topleft):
        # Imagine some nice plotting logic here...
        print('Plotting at {}, ratio {}.'.format(
            topleft, ratio))


class Polygon(Shape, Plotter):  # base class for polygons
    geometric_type = 'Polygon'

class RegularPolygon(Polygon):  # Is-A Polygon
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side


class RegularHexagon(RegularPolygon):  # Is-A RegularPolygon
    geometric_type = 'RegularHexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)


class Square(RegularPolygon):  # Is-A RegularPolygon
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side


hexagon = RegularHexagon(10)
print(hexagon.area())  # 259.8076211353316
print(hexagon.get_geometric_type())  # RegularHexagon
hexagon.plot(0.8, (75, 77))  # Plotting at (75, 77), ratio 0.8.

square = Square(12)
print(square.area())  # 144
print(square.get_geometric_type())  # Square
square.plot(0.93, (74, 75))  # Plotting at (74, 75), ratio 0.93.

print(square.__class__.__mro__)
# prints:
# (<class '__main__.Square'>, <class '__main__.RegularPolygon'>,
#  <class '__main__.Polygon'>, <class '__main__.Shape'>,
#  <class '__main__.Plotter'>, <class 'object'>)


"""
$ python multiple.inheritance.py
259.8076211353316
RegularHexagon
Plotting at (75, 77), ratio 0.8.
144
Square
Plotting at (74, 75), ratio 0.93.
(
    <class '__main__.Square'>, <class '__main__.RegularPolygon'>,
    <class '__main__.Polygon'>, <class '__main__.Shape'>,
    <class '__main__.Plotter'>, <class 'object'>
)
"""
