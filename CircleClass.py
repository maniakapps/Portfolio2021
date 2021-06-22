import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_Radius(self):
        return self.radius

    def set_radius(self,val):
        self.radius = val

    def area(self):
        return math.pi * self.radius**2




