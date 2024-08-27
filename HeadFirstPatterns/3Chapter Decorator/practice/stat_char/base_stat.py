import json


class StatCharBase:
    description: str = "Базовый класс"

    strength: int = 0
    agility: int = 0
    intelligence: int = 0
    stamina: int = 0
    spirit: int = 0

    def get_strength(self) -> int:
        return self.strength

    def get_agility(self) -> int:
        return self.agility

    def get_intelligence(self) -> int:
        return self.intelligence

    def get_stamina(self) -> int:
        return self.stamina

    def get_spirit(self) -> int:
        return self.spirit

    def get_description(self):
        return self.description

    def get_all_stat(self):
        return json.dumps(
            {
                "strength": self.get_strength(),
                "agility": self.get_agility(),
                "intelligence": self.get_intelligence(),
                "stamina": self.get_stamina(),
                "spirit": self.get_spirit(),
            }
        )
