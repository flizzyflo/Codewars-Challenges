from math import pi


class Cube:

    def __init__(self, side):
        self.side = side

    def volume(self):
        return self.side ** 3

    def surface(self):
        return self.side ** 2 * 6

    def output(self):
        print(self.volume(), self.surface())


class Ball:

    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return self.radius ** 3 * pi * 4 / 3

    def surface(self):
        return self.radius ** 2 * 4 * pi

    def output(self):
        print(self.volume(), self.surface())