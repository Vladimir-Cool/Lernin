

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

class BlaBlaException(Exception):
    pass


def subgen():
    while True:
        try:
            messages = yield
        except StopIteration:
            # print("BlaBlaBla")
            break
        else:
            print("........", messages)
    return "Return from subnet()"

@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g
    print(result)