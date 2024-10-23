
def one():
    x = ['one', 'two']
    def inner():
        print(x)
        print(id(x))
    return inner

fun_closer = one()
fun_closer()

print(fun_closer.__closure__[0].cell_contents)
print(id(fun_closer.__closure__[0].cell_contents))

class One:
    x = ['one', 'two']

    def inner(self):
        print(self.x)
        print(id(self.x))

class_one = One()
class_one.inner()
