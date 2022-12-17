from tutorial.OOP_tutorial.classes_example import Person


class Student:
    def __init__(self, name='Anonymous', age=0, score=-1):
        self.name = name
        self.age = age
        self.score = score

    def __lt__(self, other):  # less than
        if self.score < other.score:
            return True
        else:
            return False

    def __gt__(self, other):  # greater than
        if self.score > other.score:
            return True
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Student):
            return self.score + other.score
        else:
            return 0

    def __str__(self):
        return f'{self.name} is {self.age} years old and has {self.score} scores in total'


if __name__ == "__main__":
    student1 = Student()
    print(student1)

    student2 = Student('Amina', 18, 100)
    print(student2)

    print(student2 > student1)
    print(student2 < student1)

    total_score = student1 + student2
    print(f'Total score = {total_score}')

    person = Person()
    total_score2 = student1 + person
    print(total_score2)
