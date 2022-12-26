from typing import Any  # to work with data types
from dataclasses import dataclass  # decorator


@dataclass
class User:
    name: str = "name"  # not necessarily "str" - you can pass any type :-)
    age: int = "age"
    flags: list = "list"
    comment: Any = "Any"


class Admin(User):
    def get_name(self):
        return self.name


a = User(
    name="Name",
    age=17,
    flags=[1, 2, 3],
    comment=True
)

print(a)  # User(name='Name', age=17, flags=[1, 2, 3], comment=True)
print(a.flags)  # [1, 2, 3]
print(a.name)  # Name
print(a.comment)  # True

b = Admin()
print(b)  # Admin(name='name', age='age', flags='list', comment='Any')
print(b.name)  # name
print(b.get_name())  # name
print(b.__dict__)  # {'name': 'name', 'age': 'age', 'flags': 'list', 'comment': 'Any'}
