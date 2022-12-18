class Building:
    number_of_floors = 5  # defined for the entire class

    def __init__(self, name):
        self.name = name


b1 = Building("chapel")
b2 = Building("temple")

print(b1.number_of_floors)
print(Building.number_of_floors)
Building.number_of_floors = 9
print(Building.number_of_floors)
print(b2.number_of_floors)
