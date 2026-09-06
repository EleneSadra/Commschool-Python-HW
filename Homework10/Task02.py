# დავალება #10 — ამოცანა 2: თამაში 1 VS 1

# 5 მებრძოლი, თითოეულს 3 skill.
# სიცოცხლეები და დარტყმის ძალები განსხვავებულია.
# ორივე მოთამაშეს შეუძლია ერთი და იგივე გმირის არჩევა.
# ყოველ სროლაზე გამოგვაქვს მოწინააღმდეგის დარჩენილი სიცოცხლე.

import random


class Fighter:
    def __init__(self, name, health, skills):
        self.name = name
        self.max_health = health
        self.health = health
        # skills: {სახელი: დაზიანება}
        self.skills = skills

    def is_alive(self):
        return self.health > 0

    def use_skill(self, skill_name, target):
        damage = self.skills[skill_name]
        target.health -= damage
        if target.health < 0:
            target.health = 0
        print(f"\n  💥 {self.name}-მა გამოიყენა «{skill_name}» "
              f"და მიაყენა {damage} დაზიანება!")
        print(f"  ❤️  {target.name}-ს დარჩა {target.health}/{target.max_health} სიცოცხლე")

    def __str__(self):
        return f"{self.name} (HP: {self.max_health})"


# --- 5 მებრძოლი, თითოს 3 skill ---
FIGHTERS = {
    "გიგანტი": {
        "health": 160,
        "skills": {"მიწისძვრა": 22, "კლდის სროლა": 18, "ჩაგრეხვა": 25},
    },
    "სწრაფი": {
        "health": 95,
        "skills": {"ელვის დარტყმა": 30, "ორმაგი დარტყმა": 26, "ქარიშხალი": 34},
    },
    "მოქნილი": {
        "health": 115,
        "skills": {"ჩრდილის ნახტომი": 24, "ტრიალა წიხლი": 20, "ხაფანგი": 28},
    },
    "აქილევსი": {
        "health": 140,
        "skills": {"შუბის სროლა": 26, "ფარით დარტყმა": 19, "გმირული იერიში": 32},
    },
    "პითონისტი": {
        "health": 120,
        "skills": {"სინტაქსის შეცდომა": 27, "უსასრულო ციკლი": 31, "seg fault": 35},
    },
}


def choose_fighter(player_number):
    print(f"\n{'=' * 50}")
    print(f"მოთამაშე {player_number}, აირჩიე გმირი:")
    print("=" * 50)

    names = list(FIGHTERS)
    for i, name in enumerate(names, start=1):
        data = FIGHTERS[name]
        skills = ", ".join(f"{s} ({d})" for s, d in data["skills"].items())
        print(f"  {i}. {name:<12} HP: {data['health']:<5} | {skills}")

    choice = int(input("\nნომერი: ").strip())
    name = names[choice - 1]
    data = FIGHTERS[name]
    fighter = Fighter(name, data["health"], dict(data["skills"]))
    print(f"მოთამაშე {player_number}-მა აირჩია: {fighter}")
    return fighter


def choose_skill(fighter):
    print(f"\n{fighter.name}, აირჩიე skill:")
    skill_names = list(fighter.skills)
    for i, skill in enumerate(skill_names, start=1):
        print(f"  {i}. {skill} — {fighter.skills[skill]} დაზიანება")
    choice = int(input("ნომერი: ").strip())
    return skill_names[choice - 1]


def battle(f1, f2):
    print(f"\n{'=' * 50}")
    print(f"ბრძოლა იწყება: {f1.name}  VS  {f2.name}")
    print("=" * 50)

    attacker, defender = f1, f2
    round_num = 1

    while f1.is_alive() and f2.is_alive():
        print(f"\n--- რაუნდი {round_num} ---")
        skill = choose_skill(attacker)
        attacker.use_skill(skill, defender)

        if not defender.is_alive():
            break

        attacker, defender = defender, attacker   # სვლის გადაცემა
        if attacker is f1:
            round_num += 1

    winner = f1 if f1.is_alive() else f2
    print(f"\n{'=' * 50}")
    print(f"🏆 გაიმარჯვა: {winner.name}! (დარჩა {winner.health} HP)")
    print("=" * 50)


if __name__ == "__main__":
    p1 = choose_fighter(1)
    p2 = choose_fighter(2)

    # თუ ორივემ ერთი და იგივე აირჩია, სახელებს ვანომრავთ
    if p1.name == p2.name:
        p1.name += " (1)"
        p2.name += " (2)"

    battle(p1, p2)