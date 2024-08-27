from typing import Optional

from base_stat import StatCharBase


class ItemStatDecorator(StatCharBase):
    def __init__(self, stat_char_parent: Optional[StatCharBase] = None):
        self.stat_char_parent = stat_char_parent

    def get_description(self):
        return self.stat_char_parent.get_description() + self.description

    def get_strength(self) -> int:
        if self.stat_char_parent:
            if self.strength:
                return self.stat_char_parent.get_strength() + self.strength
            else:
                return self.stat_char_parent.get_strength()
        else:
            if self.strength:
                return self.strength
            else:
                return 0

    def get_agility(self) -> int:
        if self.stat_char_parent:
            if self.agility:
                return self.stat_char_parent.get_agility() + self.agility
            else:
                return self.stat_char_parent.get_agility()
        else:
            if self.agility:
                return self.agility
            else:
                return 0

    def get_intelligence(self) -> int:
        if self.stat_char_parent:
            if self.intelligence:
                return self.stat_char_parent.get_intelligence() + self.intelligence
            else:
                return self.stat_char_parent.get_intelligence()
        else:
            if self.intelligence:
                return self.intelligence
            else:
                return 0

    def get_stamina(self) -> int:
        if self.stat_char_parent:
            if self.stamina:
                return self.stat_char_parent.get_stamina() + self.stamina
            else:
                return self.stat_char_parent.get_stamina()
        else:
            if self.stamina:
                return self.stamina
            else:
                return 0

    def get_spirit(self) -> int:
        if self.stat_char_parent:
            if self.spirit:
                return self.stat_char_parent.get_spirit() + self.spirit
            else:
                return self.stat_char_parent.get_spirit()
        else:
            if self.spirit:
                return self.spirit
            else:
                return 0


class Axe(ItemStatDecorator):
    description = " с топором"
    strength = 2
    stamina = 1


class LeatherArmor(ItemStatDecorator):
    description = " в кожаной броне"
    stamina = 3


class Staff(ItemStatDecorator):
    description = " с посохом"
    intelligence = 3


class PristBook(ItemStatDecorator):
    description = " с книгой жреца"
    spirit = 3
