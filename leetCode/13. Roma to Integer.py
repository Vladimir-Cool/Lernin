class Symbol:
    symbol_list = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    num = 0

    def __init__(self, rome: str):
        self.rome = rome

    def __str__(self):
        return "Все тест"

    def roman_to_int(self):
        prev_value = 0
        for char in reversed(self.rome):
            value = self.symbol_list[char]

            if value < prev_value:
                self.num -= value
            else:
                self.num += value

            prev_value = value


test = Symbol("III")
test.roman_to_int()
print(test.num)
