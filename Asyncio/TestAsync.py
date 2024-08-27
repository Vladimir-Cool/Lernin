from time import time, sleep
import asyncio


async def sleep_func():
    print("Начало сна в 10 сек")
    await asyncio.sleep(10)
    print("сон завершен")


async def event_loop():
    tasks = []
    for i in range(3):
        task = asyncio.create_task(sleep_func())
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    t0 = time()
    asyncio.run(event_loop())
