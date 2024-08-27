from enum import Enum
from typing import Protocol


class CoffeeSize(Enum):
    TALL = 1
    GRANDE = 2
    VENTI = 3


class Beverage:
    description: str = "Unknow Beverage"
    size: CoffeeSize = CoffeeSize.TALL
    is_milk: bool
    is_soy: bool
    is_mocha: bool
    is_whip: bool

    def get_description(self) -> str:
        return self.description

    def cost(self) -> float:
        pass

    def set_size(self, size: CoffeeSize):
        self.size = size

    def get_size(self) -> CoffeeSize:
        return self.size
