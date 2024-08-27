from subject import WeatherData
from observer import CurrentConditionsDisplay

weather_data = WeatherData()
observe = CurrentConditionsDisplay(weather_data)

weather_data.set_measurements(10, 64, 30.2)
weather_data.set_measurements(11, 63, 32.2)
weather_data.set_measurements(12, 60, 28.2)
weather_data.set_measurements(13, 59, 29.2)
