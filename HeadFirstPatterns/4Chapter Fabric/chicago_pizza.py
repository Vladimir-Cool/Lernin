from typing import Optional, Type

from base_pizza import Pizza, PizzaStore
from base_pizza import (
    PepperoniIngredient,
    VeggiesIngredient,
    SauceIngredient,
    DoughIngredient,
    CheeseIngredient,
    ClamsIngredient,
)
from base_ingredient_pizza import (
    PizzaIngredientFactory,
    PlumTomatoSauce,
    ThickCrustDough,
    MozzarellaCheese,
    SlicedPepperoni,
    FrozenClams,
    BlackOlives,
    Spinach,
    EggPlant,
    Pineapple,
)


class ChicagoStyleCheesePizza(Pizza):
    def prepare(self):
        print("Подготовка сырной пиццы в стиле Чикаго")

    def bake(self):
        print("Испекание сырной пиццы в стиле Чикаго")

    def cut(self):
        print("Нарезка сырной пиццы в стиле Чикаго")

    def box(self):
        print("Упаковка сырной пиццы в стиле Чикаго")


class ChicagoStylePepperoniPizza(Pizza):
    def prepare(self):
        print("Подготовка пепперони пиццы в стиле Чикаго")

    def bake(self):
        print("Испекание пепперони пиццы в стиле Чикаго")

    def cut(self):
        print("Нарезка пепперони пиццы в стиле Чикаго")

    def box(self):
        print("Упаковка пепперони пиццы в стиле Чикаго")


class ChicagoStyleHawaiianPizza(Pizza):
    def prepare(self):
        print("Подготовка Гавайской пиццы в стиле Чикаго")

    def bake(self):
        print("Испекание Гавайской пиццы в стиле Чикаго")

    def cut(self):
        print("Нарезка Гавайской пиццы в стиле Чикаго")

    def box(self):
        print("Упаковка Гавайской пиццы в стиле Чикаго")


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> DoughIngredient:
        return ThickCrustDough()

    def create_sauce(self) -> SauceIngredient:
        return PlumTomatoSauce()

    def create_cheese(self) -> CheeseIngredient:
        return MozzarellaCheese()

    def create_veggies(self, pizza_type: str) -> Type[list[VeggiesIngredient]]:
        if pizza_type.lower() == "гавайская":
            return list[Pineapple()]

    def create_pepperoni(self) -> PepperoniIngredient:
        return SlicedPepperoni()

    def create_clams(self) -> ClamsIngredient:
        return FrozenClams()


class ChicagoStylePizzaStore(PizzaStore):
    def _create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        if pizza_type.lower() == "сырная":
            return ChicagoStyleCheesePizza()
        elif pizza_type.lower() == "пепперони":
            return ChicagoStylePepperoniPizza()
        elif pizza_type.lower() == "гавайская":
            return ChicagoStyleHawaiianPizza()
        else:
            return None
