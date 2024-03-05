import asyncio
from datetime import datetime


async def task1():
    await asyncio.sleep(2)
    print("Task 1 completed")


async def task2():
    await asyncio.sleep(5)
    print("Task 2 completed")


async def task3():
    await asyncio.gather(task1())
    await asyncio.sleep(2)
    print("Task 3 completed")


async def task4():
    await asyncio.gather(task2())
    await asyncio.sleep(7)

    print("Task 4 completed")


async def main():
    await asyncio.gather(task4(), task1(), task2(), task3())


if __name__ == "__main__":
    print(datetime.now().time())
    asyncio.run(main())
    print(datetime.now().time())
