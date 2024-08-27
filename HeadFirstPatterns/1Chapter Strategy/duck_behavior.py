from protocol_duck import FlyBehavior, QuackBehavior


class FlyWithWings(FlyBehavior):
    """Реализация полета"""

    @staticmethod
    def fly():
        print("Реализация полета")


class FlyNoWay(FlyBehavior):
    """Обычный полет"""

    @staticmethod
    def fly():
        print("Полет не реализован")


class FlyRocketPowered(FlyBehavior):
    """Полет на реактивной тяге"""

    @staticmethod
    def fly():
        print("Летит как ракета")


class Quack(QuackBehavior):
    """Реализация Кряканье"""

    @staticmethod
    def quack():
        print("Кряк")


class Squeak(QuackBehavior):
    """Реализация Пищание"""

    @staticmethod
    def quack():
        print("Увиииииии")


class MUteQuack(QuackBehavior):
    """Реализация Без кряканья"""

    @staticmethod
    def quack():
        print("-тишина-")
