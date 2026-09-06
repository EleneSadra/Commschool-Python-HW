# დავალება #9 — ამოცანა 2: მონსტრების ქარხანა

# classmethod create_from_level(level) — ეს არის "factory method" შაბლონი:
# ალტერნატიული კონსტრუქტორი, რომელიც level-ის მიხედვით ქმნის
# სხვადასხვა ტიპის მონსტრს.

# cls არის თვითონ კლასი (და არა ობიექტი), ამიტომ cls(...) ქმნის ახალ ობიექტს.

import random


class Monster:
    # level -> (ტიპი, ძალის დიაპაზონი, სპეციალობა)
    LEVEL_TABLE = {
        1: ("პაწაწინა", (5, 15), "ყვავილებს რწყავს"),
        2: ("მეგობრული", (16, 30), "ბავშვებს ეხმარება საშინაო დავალებაში"),
        3: ("მცველი", (31, 50), "ხიდებს იცავს"),
        4: ("ბრძენი", (51, 75), "რჩევებს იძლევა"),
        5: ("ლეგენდარული", (76, 100), "მთელ ქალაქს იცავს"),
    }

    def __init__(self, name, monster_type, power, specialty):
        self.name = name
        self.monster_type = monster_type
        self.power = power
        self.specialty = specialty

    @classmethod
    def create_from_level(cls, name, level):
        # ალტერნატიული კონსტრუქტორი — level-ის მიხედვით ქმნის მონსტრს.
        if level not in cls.LEVEL_TABLE:
            raise ValueError(f"დონე უნდა იყოს 1-5, მოცემულია: {level}")

        monster_type, (min_p, max_p), specialty = cls.LEVEL_TABLE[level]
        power = random.randint(min_p, max_p)
        return cls(name, monster_type, power, specialty)

    def help_human(self):
        return f"{self.name} {self.specialty} (ძალა: {self.power})"

    def __str__(self):
        return f"{self.name:<12} | {self.monster_type:<14} | ძალა: {self.power:>3}"


if __name__ == "__main__":
    random.seed(42)   # რომ შედეგი გამეორებადი იყოს

    # 10 კეთილი მონსტრი — სახელები არაა ბოროტული :)
    names_and_levels = [
        ("ბუბუ", 1), ("ლალა", 1), ("ჩიტო", 2), ("მუმუ", 2), ("პიპო", 3),
        ("ზაზა", 3), ("ნანუ", 4), ("კიკო", 4), ("ტატა", 5), ("გუგუ", 5),
    ]

    print("=" * 55)
    print("           კეთილი მონსტრების ქარხანა")
    print("=" * 55)

    monsters = []
    for name, level in names_and_levels:
        m = Monster.create_from_level(name, level)
        monsters.append(m)
        print(m)

    print("\n" + "=" * 55)
    print("           რითი ეხმარებიან ადამიანებს")
    print("=" * 55)
    for m in monsters:
        print(" -", m.help_human())

    print("\n--- ყველაზე ძლიერი ---")
    strongest = max(monsters, key=lambda m: m.power)
    print(strongest.help_human())