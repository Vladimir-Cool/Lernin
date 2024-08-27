from base_stat import StatCharBase


class WarriorStats(StatCharBase):
    description = "Воин"
    strength = 10
    agility = 5
    stamina = 10
    intelligence = 2
    spirit = 3


class RogueStats(StatCharBase):
    description = "Разбойник"
    strength = 5
    agility = 10
    stamina = 5
    intelligence = 8
    spirit = 2


class MageStats(StatCharBase):
    description = "Маг"
    strength = 3
    agility = 5
    stamina = 5
    intelligence = 10
    spirit = 7


class PristStats(StatCharBase):
    description = "Жрец"
    strength = 5
    agility = 3
    stamina = 5
    intelligence = 7
    spirit = 10
