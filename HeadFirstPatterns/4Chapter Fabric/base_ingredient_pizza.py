import abc
from typing import Protocol, Type

""" ---------CHEESE------------"""


class CheeseIngredient:
    pass


class ReggianoCheese(CheeseIngredient):
    pass


class MozzarellaCheese(CheeseIngredient):
    pass


""" ---------CHEESE END------------"""

""" ---------SAUCE------------"""


class SauceIngredient:
    pass


class MarinaraSauce(SauceIngredient):
    pass


class PlumTomatoSauce(SauceIngredient):
    pass


""" ---------SAUCE END------------"""


""" ---------DOUGH------------"""


class DoughIngredient:
    pass


class ThinCrustDough(DoughIngredient):
    pass


class ThickCrustDough(DoughIngredient):
    pass


""" ---------DOUGH END------------"""

""" ---------PEPPERONI------------"""


class PepperoniIngredient:
    pass


class SlicedPepperoni(PepperoniIngredient):
    pass


""" ---------PEPPERONI END------------"""

""" ---------CALM------------"""


class ClamsIngredient:
    pass


class FreshCalms(ClamsIngredient):
    pass


class FrozenClams(ClamsIngredient):
    pass


""" ---------CALM END------------"""

""" ---------VEGGIES------------"""


class VeggiesIngredient:
    pass


class Onion(VeggiesIngredient):
    pass


class Mushroom(VeggiesIngredient):
    pass


class RedPepper(VeggiesIngredient):
    pass


class Garlic(VeggiesIngredient):
    pass


class EggPlant(VeggiesIngredient):
    pass


class Spinach(VeggiesIngredient):
    pass


class BlackOlives(VeggiesIngredient):
    pass


class Pineapple(VeggiesIngredient):
    pass


""" ---------VEGGIES END------------"""


class PizzaIngredientFactory(Protocol):
    """Интерфейс, абстрактная фабрика для создания группы ингредиентов"""

    pizza_type: str

    @abc.abstractmethod
    def create_cheese(self) -> CheeseIngredient:
        pass

    @abc.abstractmethod
    def create_dough(self) -> DoughIngredient:
        pass

    @abc.abstractmethod
    def create_sauce(self) -> SauceIngredient:
        pass

    @abc.abstractmethod
    def create_veggies(self, veggies_set: str) -> Type[list[VeggiesIngredient]]:
        pass

    @abc.abstractmethod
    def create_pepperoni(self) -> PepperoniIngredient:
        pass

    @abc.abstractmethod
    def create_clams(self) -> ClamsIngredient:
        pass
