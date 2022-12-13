import math


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def get_area(self):
        return self.r * self.r * math.pi

    def get_perimeter(self):
        return 2 * self.r * math.pi

    def scale(self, k):
        self.r *= k

    def is_intersected(self, other) -> bool:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2
