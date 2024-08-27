class Symbol:
    symbol_list = [
        {"int": 1000, "rome": "M"},
        {"int": 900, "rome": "CM"},
        {"int": 500, "rome": "D"},
        {"int": 400, "rome": "CD"},
        {"int": 100, "rome": "C"},
        {"int": 90, "rome": "XC"},
        {"int": 50, "rome": "L"},
        {"int": 40, "rome": "XL"},
        {"int": 10, "rome": "X"},
        {"int": 9, "rome": "IX"},
        {"int": 5, "rome": "V"},
        {"int": 4, "rome": "IV"},
        {"int": 1, "rome": "I"},
    ]

    rome = ""

    def __init__(self, num: int):
        self.num = num

    def __str__(self):
        return "Все тест"

    def int_to_roman(self):
        for el in self.symbol_list:
            while self.num // el["int"] > 0:
                print(self.num)
                count = self.num // el["int"]
                self.num %= el["int"]
                self.rome += el["rome"] * count


test = Symbol(3323)
test.int_to_roman()
print(test.rome)

#
# if el["int"] == 1:
#     self.num -= el["int"]
#     self.rome += el["rome"]
# else:
