import threading
import time

from base import Singleton

singleton1 = Singleton()
singleton2 = Singleton()

assert singleton2 is singleton1
print(singleton2 is singleton1)


def thread_function():
    singleton = Singleton()
    print("Старт потока")
    time.sleep(2)
    print(id(singleton))


thread1 = threading.Thread(target=thread_function)
thread2 = threading.Thread(target=thread_function)
thread3 = threading.Thread(target=thread_function)
thread4 = threading.Thread(target=thread_function)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

print("--КОНЕЦ--")
