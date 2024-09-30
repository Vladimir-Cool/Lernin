
def new_generator(num):
    for i in range(num):
        yield "hello" + str(i)

generator = new_generator(10)

for item in generator:
    print(item)