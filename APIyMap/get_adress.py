import requests



# address = "улица Чубаровского, 79, Иркутский район"  # 52.488871, 104.306577
address = "п Грановщина	ул Евстигнеева 29 Иркутск"
api_key = "f77d6f7b-ad68-4f69-a597-4f2cf0167163"

url = f"https://geocode-maps.yandex.ru/1.x/?geocode={address}&apikey={api_key}&format=json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    coordinates = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    latitude, longitude = map(float, coordinates.split())
    print(f"{longitude}, {latitude}")
else:
    print("Адрес не найден или возникла ошибка.")
