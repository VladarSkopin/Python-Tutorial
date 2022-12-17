class Person:
    num_of_eyes = 2

    def __init__(self, name='n/a', age=0, salary=0.0):  # constructor with initial fields
        self.name = name
        self.age = age
        self.salary = salary

    def print_person(self):
        print(f'    Name: {self.name}')
        print(f'    Age: {self.age}')
        print(f'    Salary: {self.salary} $')
        print('--------------------')

    def celebrate_birthday(self):
        self.age += 1
        print(f'Yaay! Happy birthday! Now {self.name} is {self.age} years old!')


if __name__ == "__main__":
    person_1 = Person('Alex', 29, 2000)
    person_1.print_person()

    person_2 = Person()
    person_2.print_person()
