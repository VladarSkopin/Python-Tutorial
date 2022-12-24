# BUILDER DESIGN PATTERN

class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        # First goes the body
        body = self.__builder.get_body()
        car.set_body(body)

        # Then engine
        engine = self.__builder.get_engine()
        car.set_engine(engine)

        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.get_wheel()
            car.attach_wheel(wheel)
            i += 1

        return car


# The whole product
class Car:
    def __init__(self):
        self.__wheels = []
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        self.__body = body

    def attach_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d\'" % self.__wheels[0].size)


class Builder:
    def get_wheel(self): pass
    def get_engine(self): pass
    def get_body(self): pass


class JeepBuilder(Builder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def get_body(self):
        body = Body()
        body.shape = "SUV"
        return body


# Car parts
class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


jeep_builder = JeepBuilder()
director = Director()
director.set_builder(jeep_builder)
jeep = director.get_car()
jeep.specification()
