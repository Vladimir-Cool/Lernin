

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

    return average

g = average()
g.send(1)
g.send(3)
g.send(4)

#Таким исключением можно получить return Корутины и дострать значение методом .value
try:
    g.throw(StopIteration)
except StopIteration as e:
    print("Average", e.value)



