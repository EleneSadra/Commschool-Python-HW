# დავალება #10 — ამოცანა 4: ჯადოქარი

# 5 ინგრედიენტი, მომხმარებელი ირჩევს 2-ს და "ხარშავს".
# ყველა კომბინაცია განსხვავებულია.

# 5 ინგრედიენტიდან 2-ის არჩევა = C(5,2) = 10 კომბინაცია.

# ტექნიკური დეტალი: გასაღებად frozenset გამოვიყენე და არა tuple.
# frozenset-ს არ აინტერესებს თანმიმდევრობა, ამიტომ
# "ვაშლი + წყალი" და "წყალი + ვაშლი" ერთსა და იმავე რეცეპტს პოულობს.
# tuple-ით ორივე ვარიანტი ცალკე უნდა ჩამეწერა — 20 ჩანაწერი 10-ის ნაცვლად.

INGREDIENTS = ["ღამურა", "ბუმბული", "ვაშლი", "ყვავილი", "წყალი"]

RECIPES = {
    frozenset(["ღამურა", "ბუმბული"]):  "🧪 ფრენის ელექსირი",
    frozenset(["ღამურა", "ვაშლი"]):    "🍎 შხამიანი ვაშლი",
    frozenset(["ღამურა", "ყვავილი"]):  "🌙 ღამის ნექტარი",
    frozenset(["ღამურა", "წყალი"]):    "🖤 სიბნელის წვენი",
    frozenset(["ბუმბული", "ვაშლი"]):   "🍰 მსუბუქი დესერტი",
    frozenset(["ბუმბული", "ყვავილი"]): "💨 ქარის სუნამო",
    frozenset(["ბუმბული", "წყალი"]):   "☁️ ღრუბლის ნისლი",
    frozenset(["ვაშლი", "ყვავილი"]):   "🌸 ყვავილოვანი ჩირი",
    frozenset(["ვაშლი", "წყალი"]):     "🧃 ვაშლის წვენი",
    frozenset(["ყვავილი", "წყალი"]):   "🍵 ყვავილის ჩაი",
}


def show_ingredients():
    print("\nხელმისაწვდომი ინგრედიენტები:")
    for i, ingredient in enumerate(INGREDIENTS, start=1):
        print(f"  {i}. {ingredient}")


def brew(first, second):
    # ხარშავს ორ ინგრედიენტს და აბრუნებს შედეგს.
    return RECIPES[frozenset([first, second])]


if __name__ == "__main__":
    print("=" * 45)
    print("        🧙 ჯადოქრის სახელოსნო")
    print("=" * 45)

    show_ingredients()

    first_index = int(input("\nაირჩიე პირველი ინგრედიენტი (ნომერი): ").strip())
    second_index = int(input("აირჩიე მეორე ინგრედიენტი (ნომერი): ").strip())

    first = INGREDIENTS[first_index - 1]
    second = INGREDIENTS[second_index - 1]

    print(f"\nვხარშავთ: {first} + {second} ...")

    if first == second:
        print("❌ ორი ერთნაირი ინგრედიენტი არ ხარშება!")
    else:
        print(f"✨ მიიღე: {brew(first, second)}")

    # --- ყველა შესაძლო კომბინაცია ---
    print("\n" + "=" * 45)
    print("        ყველა რეცეპტი")
    print("=" * 45)

    count = 0
    for i in range(len(INGREDIENTS)):
        for j in range(i + 1, len(INGREDIENTS)):
            a, b = INGREDIENTS[i], INGREDIENTS[j]
            count += 1
            print(f"  {count:>2}. {a:<9} + {b:<9} = {brew(a, b)}")

    print(f"\n  სულ {count} კომბინაცია, ყველა განსხვავებული.")