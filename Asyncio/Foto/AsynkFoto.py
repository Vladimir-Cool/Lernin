from time import time
import asyncio
import aiohttp


async def feth_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)

def write_image(data):
    filename = "file-{}.jpeg".format(int(time() * 1000))
    with open(filename, "wb") as file:
        file.write(data)

async def main():
    url = "https://loremflickr.com/320/240"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(feth_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    t0 = time()
    asyncio.run(main())
    print(time() - t0)