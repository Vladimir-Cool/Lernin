import math


class Vector:
    """Represents a 2D vector."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # self.x!r в форматированной строке означает что вернеться строковое представление объекта repr(self.x)
    def __repr__(self):
        return f"Vector({self.x}, {self.y!r})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def get_angle(self):
        """Возвращает угол в градусах"""
        return math.atan2(self.y, self.x)


if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(0, 1)
    print(v1)
    print(abs(v1))
    print(bool(v1))
    print(v1 + v2)
    print(v1 * 3)
    print(v1.get_angle())
