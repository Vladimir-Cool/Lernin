def service_func(x: int, y: int):
    try:
        return x / y
    except ZeroDivisionError as e:
        raise


def inner_func(x: int, y: int):
    result_func = service_func(x, y)
    print("Внутренняя функция")

    return result_func


def main_func(x: int = 2, y: int = 1):
    try:
        result_func = inner_func(x, y)
        print("основная функция функция")

        return result_func
    except:
        print("Бедааа")

        return 0


print(main_func())
