from base_pizza import Pizza, PizzaIngredientFactory


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print("Готовим " + self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.сheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print("Готовим " + self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.сheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clams()


class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print("Готовим " + self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.сheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()


class HawaiianiPizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print("Готовим " + self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.сheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies("гавайская")
