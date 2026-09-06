# დავალება #8 - ამოცანა 2: ShoppingCart
# __len__() — len(cart) დააბრუნებს პროდუქტების რაოდენობას.
# __eq__()  — cart1 == cart2 შეადარებს რაოდენობებს.


class ShoppingCart:
    def __init__(self, items=None):
        # ცვალებადი (mutable) default არგუმენტი საშიშია, ამიტომ None-ს ვიყენებთ
        self.items = items if items is not None else []

    def add(self, product):
        self.items.append(product)
        return self

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        # ტიპის შემოწმება — თუ სხვა ტიპია, ვაბრუნებთ NotImplemented
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        return len(self.items) == len(other.items)

    def __repr__(self):
        return f"ShoppingCart({self.items})"


if __name__ == "__main__":
    # 2 კალათა
    c1 = ShoppingCart(["პური", "რძე"])
    c2 = ShoppingCart(["ყველი", "კვერცხი"])
    print("--- 2 კალათა ---")
    print(c1, "len =", len(c1))
    print(c2, "len =", len(c2))
    print("c1 == c2 ?", c1 == c2)          # True — ორივეში 2 პროდუქტია

    # 3 კალათა
    c3 = ShoppingCart(["წყალი"])
    print("\n--- 3 კალათა ---")
    print("c1 == c2 ?", c1 == c2)          # True
    print("c1 == c3 ?", c1 == c3)          # False — 2 vs 1
    print("c2 == c3 ?", c2 == c3)          # False

    # 4 კალათა
    c4 = ShoppingCart(["შოკოლადი"])
    print("\n--- 4 კალათა ---")
    print("c3 == c4 ?", c3 == c4)          # True — ორივეში 1
    print("c1 == c4 ?", c1 == c4)          # False

    # ყველა წყვილის შედარება ერთ ციკლში
    print("\n--- ყველა წყვილი ---")
    carts = {"c1": c1, "c2": c2, "c3": c3, "c4": c4}
    names = list(carts)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            print(f"{a} == {b} -> {carts[a] == carts[b]}")