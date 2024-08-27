import requests
import re

# num = int(input())
with open("dataset_24476_3.txt") as file:
    for num in file:
        num = int(num)
        url = f"http://numbersapi.com/{num}/math?json"
        params = {
            "callback": "showNumber"
        }

        req = requests.get(url, params=params)
        result_json = req.json()
        if result_json["found"]:
            print("Interesting")
        else:
            print("Boring")

