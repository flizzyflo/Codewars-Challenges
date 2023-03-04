
class Train:

    def __init__(self, route, start):
        self.route = route
        self.position = start

    def show_station(self):
        print(self.route[self.position])

    def move(self):
        if self.position < len(self.route) - 1:
            self.position += 1
        else:
            print("Der Zug ist im Endbahnhof angekommen!")

    def move_back(self):
        if self.position > 0:
            self.position -= 1
        else:
            print("Der Zug ist noch im Startbahnhof!")

    def bypass_station(self, station):
        self.position = 0
        self.route.remove(station)

    def add_station(self, station):
        self.position = 0
        self.route.append(station)

