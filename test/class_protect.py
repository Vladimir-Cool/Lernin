class MyClass:
    def __init__(self):
        self._private_field = 42

    @property
    def private_field(self):
        return self._private_field

    @private_field.setter
    def private_field(self, value):
        if value > 0:
            self._private_field = value
        else:
            raise ValueError("Value must be positive")


obj = MyClass()
obj._private_field = 10
print(obj.private_field)  # Доступ к приватному полю через свойство
print(obj._private_field)
obj.private_field = -1

