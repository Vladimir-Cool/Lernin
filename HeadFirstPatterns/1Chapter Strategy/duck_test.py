from duck_base import Duck
from protocol_duck import QuackBehavior, FlyBehavior
from duck_behavior import (
    FlyWithWings,
    FlyNoWay,
    Quack,
    Squeak,
    MUteQuack,
    FlyRocketPowered,
)


class MallardDuck(Duck):
    """Утка Кряква"""

    def __init__(
        self,
        name="Кряква",
        fb: FlyBehavior = FlyWithWings,
        qb: QuackBehavior = Quack,
    ):
        self.name = name
        self.fly_behavior: FlyBehavior = fb
        self.quack_behavior: QuackBehavior = qb


class RubberDuck(Duck):
    """Резиновая уточка"""

    pass


class ModelDuck(Duck):
    """Модель утки"""

    def __init__(
        self,
        name="Утра модель ракеты",
        fb: FlyBehavior = FlyNoWay,
        # qb: Optional[QuackBehavior] = None,
    ):
        self.name = name
        self.fly_behavior = fb
        # self.quack_behavior = qb


print(
    "---Определив класс поведения в конструкторе мы переопределяем поведение объекта---"
)
duck: Duck = MallardDuck("Кряква джони")
duck.swim()
duck.display()
duck.fly()

print("-------------------------------")
print("---А здесь на лету с помощью метода set переопределяем поведение")
model: Duck = ModelDuck()
model.fly()
model.set_fly_behavior(FlyRocketPowered)
model.fly()
