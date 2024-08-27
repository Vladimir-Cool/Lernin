from typing import Protocol


class Observer(Protocol):
    """Интерфейс Наблюдателя"""

    def update(self) -> None:
        pass


class Subject(Protocol):
    """Интерфейс субъекта наблюдения"""

    def register_observer(self, observer: Observer):
        pass

    def remove_observer(self, observer: Observer):
        pass

    def notify_observer(self):
        pass


class DisplayElement(Protocol):
    """Интерфейс Для отображения информации"""

    def display(self):
        pass
