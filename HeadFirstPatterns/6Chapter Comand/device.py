class Light:
    """Класс Световых приборов"""

    name: str

    def __init__(self, name: str = "Свет"):
        self.name = name

    def on(self):
        print(f"{self.name} включен")

    def off(self):
        print(f"{self.name} выключен")


class Stereo:
    """Класс стерео систем"""

    name: str
    volume: int

    def __init__(self, name: str = "Стерео система"):
        self.name = name

    def on(self):
        print(f"{self.name} включена")

    def off(self):
        print(f"{self.name} выключена")

    def set_cd(self):
        print("CD диск выбран")

    def set_volume(self, volume: int):
        self.volume = volume
        print(f"Громкость установлена в {self.volume}")


class Door:
    """Класс Дверей"""

    name: str

    def __init__(self, name: str = "Дверь"):
        self.name = name

    def open(self):
        print(f"{self.name} открыта")

    def close(self):
        print(f"{self.name} закрыта")


class Fan:
    """Класс вентиляторов"""

    @property
    def HIGH(self):
        return 3

    @property
    def MEDIUM(self):
        return 2

    @property
    def LOW(self):
        return 1

    @property
    def OFF(self):
        return

    name: str
    speer: int

    def __init__(self, name: str = "Вентилятор"):
        self.name = name
        self.speed = self.OFF

    def on(self):
        self.speed = self.MEDIUM
        print(f"{self.name} включен на скорость {self.speed}")

    def high(self):
        self.speed = self.HIGH
        print(f"Скорость переключена на {self.HIGH}")

    def medium(self):
        self.speed = self.MEDIUM
        print(f"Скорость переключена на {self.MEDIUM}")

    def low(self):
        self.speed = self.LOW
        print(f"Скорость переключена на {self.LOW}")

    def off(self):
        self.speed = self.OFF
        print(f"{self.name} выключен")

    def get_speed(self):
        return self.speed
