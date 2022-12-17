class Person:
    def __init__(self):  # constructor with initial fields
        self.name = "n/a"
        self.age = 0
        self.salary = 0.0

    def print_person(self):
        print(f'    Name: {self.name}')
        print(f'    Age: {self.age}')
        print(f'    Salary: {self.salary} $')
        print('--------------------')

    def celebrate_birthday(self):
        self.age += 1
        print(f'Yaay! Happy birthday! Now {self.name} is {self.age} years old!')


if __name__ == "__main__":
    person_A = Person()
    person_A.celebrate_birthday()
    person_A.print_person()

    person_B = Person()
    person_B.name = 'Alex'
    person_B.age = 29
    person_B.salary = 2000
    person_B.celebrate_birthday()
    person_B.print_person()


