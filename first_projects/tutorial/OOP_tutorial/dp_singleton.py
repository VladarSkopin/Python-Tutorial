# SINGLETON DESIGN PATTERN

class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


s = Singleton()
print(s)

s1 = Singleton.get_instance()
print(s1)

s2 = Singleton.get_instance()
print(s2)

b = Singleton()
print(b)


