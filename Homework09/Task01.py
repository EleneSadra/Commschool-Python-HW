# დავალება #9 — ამოცანა 1: თამაში

# Character მშობელი კლასი -> Warrior, Mage, Archer მემკვიდრეები.
# super()-ით ვიძახებთ მშობლის კონსტრუქტორს.

# უპირატესობის წრე (ქვა-მაკრატელი-ქაღალდის პრინციპი):
#     Warrior  სჯობს  Mage
#     Mage     სჯობს  Archer
#     Archer   სჯობს  Warrior


class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    # ვისზე აქვს უპირატესობა — მემკვიდრეები გადაფარავენ
    beats = None

    def is_alive(self):
        return self.health > 0

    def attack(self, target):
        # ესხმის თავს მოწინააღმდეგეს.
        # თუ ამ კლასს უპირატესობა აქვს მოწინააღმდეგეზე — ორმაგი დაზიანება.
        damage = self.strength
        if self.beats == type(target).__name__:
            damage *= 2
            print(f"  {self.name} ({type(self).__name__}) უპირატესობით ესხმის "
                  f"{target.name}-ს ({type(target).__name__})! დაზიანება: {damage}")
        else:
            print(f"  {self.name} ({type(self).__name__}) ესხმის "
                  f"{target.name}-ს. დაზიანება: {damage}")

        target.health -= damage
        if target.health < 0:
            target.health = 0
        print(f"  {target.name}-ს დარჩა {target.health} სიცოცხლე")

    def __str__(self):
        return f"{self.name} ({type(self).__name__}) HP={self.health} STR={self.strength}"


class Warrior(Character):
    beats = "Mage"

    def __init__(self, name):
        super().__init__(name, health=120, strength=15)


class Mage(Character):
    beats = "Archer"

    def __init__(self, name):
        super().__init__(name, health=90, strength=20)


class Archer(Character):
    beats = "Warrior"

    def __init__(self, name):
        super().__init__(name, health=100, strength=18)


def fight(a, b):
    # ორი გმირი ებრძვის ერთმანეთს, სანამ ერთ-ერთს სიცოცხლე არ გაუთავდება.
    print(f"\n{'=' * 60}")
    print(f"ბრძოლა: {a}  VS  {b}")
    print("=" * 60)

    round_num = 1
    while a.is_alive() and b.is_alive():
        print(f"\nრაუნდი {round_num}:")
        a.attack(b)
        if not b.is_alive():
            break
        b.attack(a)
        round_num += 1

    winner = a if a.is_alive() else b
    loser = b if a.is_alive() else a
    print(f"\n>>> გაიმარჯვა: {winner.name} ({type(winner).__name__})")
    print(f">>> დამარცხდა: {loser.name} ({type(loser).__name__})")
    return winner


if __name__ == "__main__":
    # სამივე ვარიანტი — ყოველ ჯერზე უპირატესობის მქონე უნდა გაიმარჯვოს

    # 1. Warrior სჯობს Mage-ს
    fight(Warrior("ელენე"), Mage("მანონი"))

    # 2. Mage სჯობს Archer-ს
    fight(Mage("გენდალფი"), Archer("ლეგოლასი"))

    # 3. Archer სჯობს Warrior-ს
    fight(Archer("რობინ ჰუდი"), Warrior("ეილინი"))