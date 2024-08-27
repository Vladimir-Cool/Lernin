from protocol_duck import QuackBehavior, FlyBehavior


class Duck:
    """Базовый класс 'Утки'"""

    name: str
    fly_behavior: FlyBehavior
    quack_behavior: QuackBehavior

    def display(self):
        print(f"Это {self.name}")

    def swim(self):
        print(f"{self.name} плывет")

    def fly(self):
        """Функция делегирует поведение классу поддерживаемому интерфейс FlyBehavior"""
        return self.fly_behavior.fly()

    def quack(self):
        """Функция делегирует поведение классу поддерживаемому интерфейс QuackBehavior"""
        return self.quack_behavior.quack()

    def set_fly_behavior(self, fb: FlyBehavior):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior):
        self.quack_behavior = qb
