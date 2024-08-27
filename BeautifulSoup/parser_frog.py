from time import time
import requests
from bs4 import BeautifulSoup


def feth_content(url):
    HEADERS = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36",
        "X-Yandex-API-Key": "74faec16-b2b4-4d33-9597-2fa749fb41be",
    }
    response = requests.get(url, headers=HEADERS)

    bs = BeautifulSoup(response.content, "lxml")
    # print(bs.body)
    print(bs.body.find_all("a", recursive=True))


def write_image(data):
    filename = "file-{}.jpeg".format(int(time() * 1000))
    with open(filename, "wb") as file:
        file.write(data)


if __name__ == "__main__":
    search_word = "лягушка"
    url = f"https://yandex.ru/images/search?text={search_word}"
    feth_content(url)
