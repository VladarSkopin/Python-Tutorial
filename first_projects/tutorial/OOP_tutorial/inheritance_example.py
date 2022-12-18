class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def speak(self):
        print('I\'m not sure I can speak')


class Cat(Pet):  # inheriting from Pet class
    def __init__(self, name, age, color):
        super().__init__(name, age)  # no need to pass "self"!
        self.color = color
        # self.name = name
        # self.age = age

    def speak(self):  # will automatically override the parent method
        print('Meow')

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')


class Dog(Pet):

    def speak(self):  # override
        print('Bark!')


class Fish(Pet):
    pass


p = Pet('Snowball', 1000)
p.show()
p.speak()
c = Cat('Scrapy', 7, 'brown')
c.show()
c.speak()
d = Dog('Patrik', 12)
d.show()
d.speak()
f = Fish('Bubbles', 1)
f.show()
f.speak()  # calling the parent method (not defined in the Fish class)
