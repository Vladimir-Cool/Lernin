from base_coffe import Beverage


class ComdimentDecorator(Beverage):
    beverage: Beverage

    def get_description(self):
        return super().get_description()


class Milk(ComdimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Milk"

    def cost(self):
        return self.beverage.cost() + 0.10


class Mocha(ComdimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + 0.20


class Soy(ComdimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return self.beverage.cost() + 0.15


class Whip(ComdimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return self.beverage.cost() + 0.10
