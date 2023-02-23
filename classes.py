class Point:

    default_color = "green"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0,0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# point = Point()
# print(isinstance(point, Point))
# Instance variables can be changed on the fly.

point = Point.zero()
point2 = Point(5, 10)
print(point.default_color)
point.draw()
point2.draw()
Point.default_color = "Mint"

print(point.default_color)
print(point2.default_color)
