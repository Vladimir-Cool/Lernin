from functools import lru_cache
from time import time

def my_decorator(arg_1=0):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Сделаей что то до вызова {arg_1}")
            result = func(*args, **kwargs)
            print(f"Сделаей что то после вызова {arg_1}")
            return result
        return wrapper
    return my_decorator


@my_decorator(arg_1=10)
def func_test():
    return "hello"

#-----------------------------------
@lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

time_start = time()
result = fibonacci(37)
time_delta = time() - time_start

print(time_delta)



class StaticClass:
    @staticmethod
    def get_result():
        return "result"


print(StaticClass.get_result())


class PropsClass:
    @property
    def get_props(self):
        print("Props")

prop = PropsClass()
prop.get_props
