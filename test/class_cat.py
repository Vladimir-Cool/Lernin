
class animal:
    pass


class Cat:
    """ Класс животного Кот"""
    __name = ""
    color = ""
    voice = ""

    def __init__(self, name, color, voice="Мяу"):
        self.__name = name
        self.color = color
        self.voice = voice

    def __get_voice(self):
        print(f"{self.__name} говорит {self.voice}")

    def voice(self):
        self.__get_voice()

cat = Cat("Борис", "Черный")

# cat.__get_voice()
# print(cat.__name)


print(cat._Cat__get_voice())
print(cat._Cat__name)

print(dir(Cat))
