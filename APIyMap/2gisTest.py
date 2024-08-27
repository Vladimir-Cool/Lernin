import requests
import json


def get_token():
    client_id = "d1273cf7f24fede5a40d"
    client_secret = "2f4fc45215db6ce6fcf610dbb75fc65d"
    r = requests.post(
        "https://api.artsy.net/api/tokens/xapp_token",
        data={"client_id": client_id, "client_secret": client_secret},
    )

    j = json.loads(r.text)
    return j["token"]


token = get_token()
art_list = []

url = "https://2gis.ru/irkutsk/search/"

r = requests.post(url + "иркутская область тулун улица Надежды дом 7")
print(r)
