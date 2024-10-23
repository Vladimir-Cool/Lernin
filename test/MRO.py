
class One:
    message = "one"


class Two:
    message = "two"


class MROTest(One, Two):
    pass


class MROTest2(Two, One):
    pass


a = MROTest()
print(MROTest.mro())
print(a.message)

a2 = MROTest2()
print(MROTest2.mro())
print(a2.message)
