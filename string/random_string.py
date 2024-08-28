import random

letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
symbols = "!@#$%&?"
numbers = "0123456789"

def get_random_string(leanght: int = 8) -> str:
    """ Возвращает строку из случайных символов
        leanght: длина получаемой строки.
    """

    def generate_reliable_str(leanght: int) -> str:
        """ Создает новую строку со случайными символами"""
        new_str = ""
        selection = letters + symbols + numbers

        for i in range(leanght):
            new_str += random.choice(selection)
        return new_str


    def check_reliable(new_str: str) -> bool:
        """Проверяет чтобы в новую строку входили как минимум одна буква, одна цифра и один символ"""
        check_dict = {
            "letters": 0,
            "symbols": 0,
            "numbers": 0
        }

        for el in new_str:
            if el in letters:
                check_dict["letters"] += 1
            elif el in symbols:
                check_dict["symbols"] += 1
            elif el in numbers:
                check_dict["numbers"] += 1

        if check_dict["letters"] and check_dict["symbols"] and check_dict["numbers"]:
            return True
        return False

    #
    if leanght < 3:
        raise Exception("минимальная длина пароля 3 символа")


    new_str = generate_reliable_str(leanght)
    while True:
        if check_reliable(new_str):
            return new_str

        new_str = generate_reliable_str(leanght)



print(get_random_string(4))