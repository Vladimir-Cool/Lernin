from base_turkey import WildTurkey
from base_duck import MallardDuck, Duck
from adapter import TurkeyAdapterToDuck


def test_duck(duck: Duck) -> None:
    duck.quack()
    duck.fly()


duck = MallardDuck()

turkey = WildTurkey()
turkey_adapter: Duck = TurkeyAdapterToDuck(turkey)

print("ТЕст индюка")
turkey.gobble()
turkey.fly()

print("ТЕст утки")
test_duck(duck)

print("ТЕст индюка в адапторе")
test_duck(turkey_adapter)
