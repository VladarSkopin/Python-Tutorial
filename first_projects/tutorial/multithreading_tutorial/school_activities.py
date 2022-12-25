import threading
import time


def eat_breakfast(**kwargs):
    food = kwargs.get('food')
    time.sleep(3)
    print(f"You ate breakfast: {food}")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finished studying")


x = threading.Thread(target=eat_breakfast, kwargs={'food': 'eggs'})
x.start()

y = threading.Thread(target=drink_coffee)
y.start()

z = threading.Thread(target=study)
z.start()

# THREAD SYNCHRONIZATION - wait for thread to finish = join()
x.join()
y.join()
z.join()

print(__name__)  # __main__
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
