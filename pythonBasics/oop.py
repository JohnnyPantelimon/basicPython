class Robot:
    Population = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Robot.Population += 1

    def __del__(self):
        print(f"Robot {self.name} has been removed")

    def __add__(self, other):
        return self.price + other.price

    def __gt__(self, other):
        if self.price > other.price:
            return f"Robot {self.name} is bigger than {other.name}"
        return f"Robot {other.name} is bigger than {self.name}"



r1 = Robot("Marvin", 150)
r2 = Robot("Gal", 45)

print(r1 + r2)
print(r1 > r2)










# class Robot:
#     """This class implements a Robot"""
#     population = 0
#
#     def __init__(self,name, build_year):
#         self.name = name
#         self.build_year = build_year
#         Robot.population += 1
#
#     def __str__(self):
#         return f"This robot is called {self.name} and was created in {self.build_year}"
#
#     def __repr__(self):
#         return f"Robot's name is {self.name} and was born in {self.build_year}"
#
#     def setEnergy(self, energy):
#         self.energy = energy
#
#
# r1 = Robot("Robo", 1900)
#
# print(r1.__doc__)
# print(r1.name, "->", r1.build_year)
# print(r1)
# r1.setEnergy(500)
# print(r1.energy)
#
# r2 = Robot("Robocop", 2000)
# print(r2.name, "->", r1.build_year)
# print(r2)
# r2.setEnergy(1500)
# print(r2.energy)
#
# print(r2.population)