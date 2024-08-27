from protocol import Observer, DisplayElement, Subject


class CurrentConditionsDisplay(Observer, DisplayElement):
    """Класс который выводит температуру и влажность"""

    temperature: float
    humidity: float
    weather_data: Subject

    def __init__(self, weather_data: Subject) -> None:
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self) -> None:
        self.temperature = self.weather_data.get_temperature()
        self.humidity = self.weather_data.get_humidity()
        self.display()

    def display(self) -> None:
        print(
            f"Данные выведены:\nТемпература {self.temperature}К\nВлажность {self.humidity}%"
        )
