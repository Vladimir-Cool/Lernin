import requests
import json


def get_token():
    client_id = 'd1273cf7f24fede5a40d'
    client_secret = '2f4fc45215db6ce6fcf610dbb75fc65d'
    r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                      data={
                          "client_id": client_id,
                          "client_secret": client_secret
                      })

    j = json.loads(r.text)
    return j['token']

def sort_two(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j]["birthday"] > list[j+1]["birthday"]:
                list[j], list[j + 1] = list[j+1], list[j]

            elif list[j]["birthday"] == list[j+1]["birthday"]:

                if list[j]["name"] > list[j + 1]["name"]:
                    list[j], list[j + 1] = list[j + 1], list[j]

token = get_token()
art_list = []

with open("dataset_24476_4(1).txt") as file:
    for id_art in file:
        headers = {"X-Xapp-Token": token}
        r = requests.get(f"https://api.artsy.net/api/artists/{id_art[:-1]}", headers=headers)
        j = json.loads(r.text)
        # art_list.append({"name": j["name"], "birthday": j["birthday"]})
        art_list.append((j["sortable_name"], j["birthday"]))


print(art_list)

# print(sorted(art_list, key=lambda x : x["birthday"]))
sorted_list = sorted(art_list, key=lambda x: (x[1], x[0]))
for i in sorted_list:
    print(i[0])

