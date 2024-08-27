from time import time
import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def feth_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        # data = await response.read()
        bs = BeautifulSoup(response.read(), "lxml")
        print(bs)


def write_image(data):
    filename = "file-{}.jpeg".format(int(time() * 1000))
    with open(filename, "wb") as file:
        file.write(data)


async def main(url: str):
    async with aiohttp.ClientSession() as session:
        task = asyncio.create_task(feth_content(url, session))
        await asyncio.gather(task)


if __name__ == "__main__":
    search_word = "лягушка"
    url = f"https://yandex.ru/images/search?from=tabbar&text={search_word}"

    asyncio.run(main(url))
