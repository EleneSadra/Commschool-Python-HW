# დავალება #8 — ამოცანა 6: CustomList

# __getitem__() — cl[0]
# __setitem__() — cl[0] = "ახალი"
# __iter__()    — for x in cl

# __iter__-ს უნდა დააბრუნოს იტერატორი. აქ yield-ს ვიყენებთ,
# რაც ფუნქციას გენერატორად აქცევს — ეს ყველაზე მოკლე გზაა.


class CustomList:
    def __init__(self, elements=None):
        self._elements = list(elements) if elements else []

    def append(self, value):
        self._elements.append(value)

    def __getitem__(self, index):
        return self._elements[index]

    def __setitem__(self, index, value):
        self._elements[index] = value

    def __iter__(self):
        for item in self._elements:
            yield item

    def __len__(self):
        return len(self._elements)

    def __repr__(self):
        return f"CustomList({self._elements})"


if __name__ == "__main__":
    cl = CustomList(["ვაშლი", "ბანანი", "მსხალი"])
    print(cl)

    print("\n--- __getitem__ ---")
    print("cl[0] =", cl[0])
    print("cl[2] =", cl[2])
    print("cl[-1] =", cl[-1])        # უარყოფითი ინდექსი უფასოდ მუშაობს

    print("\n--- __setitem__ ---")
    cl[1] = "ატამი"
    print("cl[1]-ის შეცვლის შემდეგ:", cl)

    print("\n--- __iter__ (for ციკლი) ---")
    for fruit in cl:
        print("  -", fruit)

    print("\n--- სხვა რამაც უფასოდ იმუშავა ---")
    cl.append("ლიმონი")
    print("len(cl) =", len(cl))
    print("list(cl) =", list(cl))
    print("'ატამი' in cl ->", "ატამი" in cl)   # in მუშაობს __iter__-ის წყალობით
    print("enumerate:")
    for i, fruit in enumerate(cl):
        print(f"  {i}: {fruit}")