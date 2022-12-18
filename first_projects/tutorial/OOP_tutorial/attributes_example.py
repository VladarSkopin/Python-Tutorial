class Building:
    number_of_floors = 5  # defined for the entire class
    __number_of_buildings = 0  # class variable (hidden)

    def __init__(self, name):
        self.name = name
        Building.__number_of_buildings += 1

    @classmethod
    def get_number_of_buildings(cls):  # method belongs to the whole class rather than instance
        return cls.__number_of_buildings

    @classmethod
    def add_building(cls):
        cls.__number_of_buildings += 1


b1 = Building("chapel")
b2 = Building("temple")
print(f'Buildings = {Building.get_number_of_buildings()}')
Building.add_building()
print(f'Buildings = {Building.get_number_of_buildings()}')
