import asyncio
import json


async def data2(name, price):
    with open("data2.json", "w") as f:
        json.dump({"name": name, "price": price}, f, indent=6)


async def data1():
    with open("data1.json", "r") as file:
        data = json.load(file)
        print("Ma'lumotlar o'qildi")
        name = []
        price = []
        for i in data["courses"]:
            name.append(i["name"])
            price.append(i["price"])
        await data2(name, price)


asyncio.run(data1())
