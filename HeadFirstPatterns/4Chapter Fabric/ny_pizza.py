from abc import ABC, ABCMeta
from typing import Optional, Type

from base_pizza import PizzaStore, Pizza
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
    Onion,
    Mushroom,
    RedPepper,
    Garlic,
    ThinCrustDough,
    MarinaraSauce,
    ReggianoCheese,
    SlicedPepperoni,
    FreshCalms,
    Pineapple,
)
from different_pizzas import CheesePizza, PepperoniPizza, HawaiianiPizza, ClamPizza


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> DoughIngredient:
        return ThinCrustDough()

    def create_sauce(self) -> SauceIngredient:
        return MarinaraSauce()

    def create_cheese(self) -> CheeseIngredient:
        return ReggianoCheese()

    def create_veggies(self, pizza_type) -> Type[list[VeggiesIngredient]]:
        if pizza_type.lower() == "гавайская":
            return list[Pineapple(), Onion()]
        else:
            return list[Onion(), Mushroom(), RedPepper(), Garlic()]

    def create_pepperoni(self) -> PepperoniIngredient:
        return SlicedPepperoni()

    def create_clams(self) -> ClamsIngredient:
        return FreshCalms()


class NYStylePizzaStore(PizzaStore):
    def _create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if pizza_type.lower() == "сырная":
            pizza = CheesePizza(ingredient_factory)

            pizza.name = "Сырная пицца по Н-Йорски"

        elif pizza_type.lower() == "пепперони":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.name = "Пицца пепперони по Н-Йорски"

        elif pizza_type.lower() == "гавайская":
            pizza = HawaiianiPizza(ingredient_factory)
            pizza.name = "Гавайская пицца по Н-Йорски"

        elif pizza_type.lower() == "мидии":
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "Пицца с мидиями по Н-Йорски"

        else:
            return None

        return pizza
