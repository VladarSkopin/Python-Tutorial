# CLASS DECORATOR

# __call__ -> returns object that acts as a function

from time import time


class Timer:
    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):
        start_time = time()
        result = self.function(*args, **kwargs)
        end_time = time()
        print("Execution took {} seconds".format(end_time - start_time))
        return result


@Timer
def some_function(delay):
    from time import sleep
    # time delay simulation
    sleep(delay)


some_function(3)
