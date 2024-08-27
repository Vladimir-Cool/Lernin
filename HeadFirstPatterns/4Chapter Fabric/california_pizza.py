from typing import Optional

from base_pizza import Pizza, PizzaStore


class CaliforniaStyleCheesePizza(Pizza):
    def prepare(self):
        print("Подготовка сырной пиццы в стиле Калифорнии")

    def bake(self):
        print("Испекание сырной пиццы в стиле Калифорнии")

    def cut(self):
        print("Нарезка сырной пиццы в стиле Калифорнии")

    def box(self):
        print("Упаковка сырной пиццы в стиле Калифорнии")


class CaliforniaStylePepperoniPizza(Pizza):
    def prepare(self):
        print("Подготовка пепперони пиццы в стиле Калифорнии")

    def bake(self):
        print("Испекание пепперони пиццы в стиле Калифорнии")

    def cut(self):
        print("Нарезка пепперони пиццы в стиле Калифорнии")

    def box(self):
        print("Упаковка пепперони пиццы в стиле Калифорнии")


class CaliforniaStyleHawaiianPizza(Pizza):
    def prepare(self):
        print("Подготовка Гавайской пиццы в стиле Калифорнии")

    def bake(self):
        print("Испекание Гавайской пиццы в стиле Калифорнии")

    def cut(self):
        print("Нарезка Гавайской пиццы в стиле Калифорнии")

    def box(self):
        print("Упаковка Гавайской пиццы в стиле Калифорнии")


class CaliforniaStylePizzaStore(PizzaStore):
    def _create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        if pizza_type.lower() == "сырная":
            return CaliforniaStyleCheesePizza()
        elif pizza_type.lower() == "пепперони":
            return CaliforniaStylePepperoniPizza()
        elif pizza_type.lower() == "гавайская":
            return CaliforniaStyleHawaiianPizza()
        else:
            return None
