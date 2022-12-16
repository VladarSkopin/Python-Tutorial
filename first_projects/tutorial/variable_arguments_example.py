"""
def print_person(name, age=0, *args):
    print(name, age)
    for extra in args:
        print(extra)
    print('-----')


print_person('Bob', 45, 200, 'engineer')
print_person('Alex', 29, 52, 'tester')
print_person('Kitty', 24, 'Student')
print_person('Just some guy')
"""


def print_person(name, age=0, **kwargs):
    print(name, age)
    for data, extra in kwargs.items():
        print(data, ':', extra)


print_person('Alex', 32, salary=890_000, job='programmer')
