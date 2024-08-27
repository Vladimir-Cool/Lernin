

class Soda:
    def __init__(self, taste=None):
        if isinstance(taste, str):
            self.taste = taste
        else:
            self.taste = None

    def show_my_drink(self):
        if self.taste:
            print(f"Газировка со вкусом {self.taste}")
        else:
            print("Обычняа газировка")

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if type(self.a) != int or type(self.b) != int or type(self.c) != int:
            print("Нужно вводить только числа!; ")
        elif self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            print("Ура, можно построить треугольник!")
        elif self.a < 0 or self.b < 0 or self.c < 0:
            print("С отрицательными числами ничего не выйдет!")
        else:
            print(" Жаль, но из этого треугольник не сделать. ")


class KgToPounds:
    def __init__(self, kg):
        if isinstance(kg, (int, float)):
            self.__kg = kg
        else:
            print("Нужно ввести число")

    def to_pounds(self):
        return self.__kg * 2.205

    def __set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            print("Нужно ввести число")

    def __get_kg(self):
        return self.__kg

    kg = property(__get_kg, __set_kg)
    # property(fget, fset, fdel, doc)

class KgToPoundsDecorator:
    def __init__(self, kg):
        if isinstance(kg, (int, float)):
            self.__kg = kg
        else:
            print("Нужно ввести число")

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            print("Нужно ввести число")

class Nikola:
    __slots__ = ["__name", "__age"]

    def __init__(self, name, age):
        if name == "Николай":
            self.__name = name
        else:
            print(f"я не {name}, а Николай")
            self.__name = "Николай"
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "Николай":
            self.__name = new_name
        else:
            print(f"я не {new_name}, а Николай")
            self.__name = "Николай"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

class RealString:
    def __init__(self, st):
        if isinstance(st, str):
            self.st = st
        else:
            print("Ошибка, нужно ввести строку")

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self.st) == len(other.st)
        return False

    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self.st) < len(other.st)
        return False

    def __gt__(self, other):
        if isinstance(other, RealString):
            return len(self.st) > len(other.st)
        return False


str1 = RealString("дв")
str2 = RealString("три")
print(str1 == str2)
print(str1 < str2)
print(str1 > str2)


