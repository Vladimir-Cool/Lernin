import abc
from typing import Protocol, Type
from base_ingredient_pizza import (
    PizzaIngredientFactory,
    DoughIngredient,
    SauceIngredient,
    VeggiesIngredient,
    PepperoniIngredient,
    CheeseIngredient,
    ClamsIngredient,
)


class Pizza(Protocol):
    name: str = "Пицца"
    dough: DoughIngredient
    sauce: SauceIngredient
    veggies: list[VeggiesIngredient]
    pepperoni: PepperoniIngredient
    cheese: CheeseIngredient
    clams: ClamsIngredient

    @abc.abstractmethod
    def prepare(self) -> None:
        pass

    def bake(self) -> None:
        print("Выпекать 25 минут при температуре 350.")

    def cut(self) -> None:
        print("Разрезаем пиццу на диагональные ломтики")

    def box(self) -> None:
        print("Поместите пиццу в официальную коробку PizzaStore.")

    def __str__(self):
        return self.name


class PizzaStore:
    @abc.abstractmethod
    def _create_pizza(self, pizza_type: str) -> Pizza:
        pass

    def order_pizza(self, pizza_type: str) -> Pizza:
        self.pizza = self._create_pizza(pizza_type)

        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()
        return self.pizza


# class CheesePizza(Pizza):
#     def prepare(self):
#         print("Подготовка сырной пиццы")
#
#     def bake(self):
#         print("Испекание сырной пиццы")
#
#     def cut(self):
#         print("Нарезка сырной пиццы")
#
#     def box(self):
#         print("Упаковка сырной пиццы")
#
#
# class PepperoniPizza(Pizza):
#     def prepare(self):
#         print("Подготовка пепперони пиццы")
#
#     def bake(self):
#         print("Испекание пепперони пиццы")
#
#     def cut(self):
#         print("Нарезка пепперони пиццы")
#
#     def box(self):
#         print("Упаковка пепперони пиццы")
#
#
# class HawaiianPizza(Pizza):
#     def prepare(self):
#         print("Подготовка Гавайской пиццы")
#
#     def bake(self):
#         print("Испекание Гавайской пиццы")
#
#     def cut(self):
#         print("Нарезка Гавайской пиццы")
#
#     def box(self):
#         print("Упаковка Гавайской пиццы")
#
#
# class SimplePizzaFactory:
#     def create_pizza(self, pizza_type: str) -> Pizza:
#         if pizza_type.lower() == "сырная":
#             pizza = CheesePizza()
#         elif pizza_type.lower() == "пепперони":
#             pizza = PepperoniPizza()
#         elif pizza_type.lower() == "говайская":
#             pizza = HawaiianPizza()
#
#         return pizza
