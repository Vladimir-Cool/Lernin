# Декоратор который инициирует корутину
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


@coroutine
def average():
    """Тест корутины"""
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)


# g=average()     #Cоздание корутины
# g.send(None)    #Активация перенесена в декоратор
#
# g.send(1)       #Передаем значение и сразу получаем средний результат
# g.send(2)
# g.send(3)
#
# g.throw(StopIteration)  #Передаем ошибку и завершаем работу корутины
