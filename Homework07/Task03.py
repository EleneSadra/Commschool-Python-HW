import json

table = [
{"id": 1, "price": 50},
{"id": 2, "price": 200},
{"id": 3, "price": 150}
]

for product in table:
    if product["price"] > 100:
        print(product)