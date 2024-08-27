from base_coffe import Beverage


class HoseBlend(Beverage):
    def get_description(self) -> str:
        self.description = "House Blend Coffe"
        return self.description

    def cost(self) -> float:
        return 0.89


class DarkRoast(Beverage):
    def get_description(self) -> str:
        self.description = "Темная обжарка"
        return self.description

    def cost(self) -> float:
        return 0.99


class Espresso(Beverage):
    def get_description(self) -> str:
        self.description = "Espresso"
        return self.description

    def cost(self) -> float:
        return 1.99


class Decaf(Beverage):
    def get_description(self) -> str:
        self.description = "без кофеина"
        return self.description

    def cost(self) -> float:
        return 1.05
