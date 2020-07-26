import math

class Sphere:
    def __init__(self, *args):
        if args:
            self.setRadius(args[0])
        else:
            self.setRadius(1.0)

    def setRadius(self, newRadius):
        if newRadius >= 0.0:
            self.theRadius = newRadius

    def diameter(self):
        return self.radius() * 2

    def radius(self):
        return self.theRadius
    
    def circumference(self):
        return math.pi * 2 * self.radius()

    def area(self):
        return math.pi * math.pi * self.radius()

    def volume(self):
        return (4.0 * math.pi * math.pow(self.radius(), 3.0)) / 3.0

    def displayStatistics(self):
        radius = self.radius()
        diameter = self.diameter()
        print(f'Radius= {self.radius()} \nDiameter= {self.diameter()} \nCircumference= {self.circumference()} \nArea= {self.area()} \nVolume= {self.volume()}')

class Ball(Sphere):
    def __init__(self, *args):
        if args:
            super().__init__(args[0])
            self.setName(args[1])
        else:
            super().__init__()
            self.setName("unknown")

    def setName(self, newName):
        self.theName = newName
    
    def name(self):
        return self.theName

    def displayStatistics(self):
        print(f'\nStatistics for a {self.name()}', end="")
        return super().displayStatistics()

sphere1 = Sphere(5)
sphere1.displayStatistics()

ball1 = Ball(6, "ball")
ball1.displayStatistics()