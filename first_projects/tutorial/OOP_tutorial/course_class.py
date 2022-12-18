from tutorial.OOP_tutorial.class_customization_example import Student


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_score()  # student.score
        return value / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Lora", 20, 67)
s3 = Student("Bill")

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0])
print(course.students[0].name)
print(course.get_average_grade())
print(course.add_student(s3))
