# დავალება #8 — ამოცანა 7: Refrigerator

# __contains__() — "milk" in fridge
# __str__()      — print(fridge) -> "Fridge with N items"
# __del__()      — "Fridge unplugged!"


class Refrigerator:
    def __init__(self, items=None):
        self.items = list(items) if items else []

    def add(self, product):
        self.items.append(product)
        print(f"დაემატა: {product}")

    def __contains__(self, product):
        # იძახება in ოპერატორისთვის.
        return product in self.items

    def __str__(self):
        return f"Fridge with {len(self.items)} items"

    def __del__(self):
        print("Fridge unplugged!")


if __name__ == "__main__":
    fridge = Refrigerator()

    print("--- პროდუქტების დამატება ---")
    for product in ["milk", "cheese", "eggs", "butter"]:
        fridge.add(product)

    print("\n--- __contains__ ---")
    print('"milk" in fridge   ->', "milk" in fridge)
    print('"pizza" in fridge  ->', "pizza" in fridge)

    print("\n--- __str__ ---")
    print(fridge)

    print("\n--- __del__ ---")
    del fridge
    print("მაცივარი წაშლილია.")