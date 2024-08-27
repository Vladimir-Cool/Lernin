from protocol import Subject, Observer
from typing import Optional


class WeatherData(Subject):
    """Класс для сбора показаний погоды"""

    observers: set[Optional[Observer]]
    temperature: float
    humidity: float
    pressure: float

    def __init__(self):
        self.observers = set()

    def register_observer(self, observer: Observer):
        self.observers.add(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observer(self):
        if self.observers:
            for observer in self.observers:
                observer.update()

    def measurements_changed(self):
        self.notify_observer()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

    def get_temperature(self) -> float:
        return self.temperature

    def get_humidity(self) -> float:
        return self.humidity

    def get_pressure(self) -> float:
        return self.pressure
