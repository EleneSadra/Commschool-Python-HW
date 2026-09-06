# დავალება #9 — ამოცანა 4: გმირის ქულების სისტემა

# აერთიანებს ყველაფერს:
#   private health / score  — ენკაფსულაცია
#   staticmethod            — random_event()
#   classmethod             — from_name()
#   მემკვიდრეობა            — SuperHero(Hero)
#   super()                 — მშობლის კონსტრუქტორის გამოძახება

import random


class Hero:
    EVENTS = [
        ("იპოვე განძი", "score", +10),
        ("დაამარცხე მონსტრი", "score", +15),
        ("გადაარჩინე სოფელი", "score", +25),
        ("ჩავარდი ორმოში", "health", -20),
        ("მოწინააღმდეგემ დაგარტყა", "health", -15),
        ("მოწამლული საკვები შეჭამე", "health", -10),
    ]

    def __init__(self, name, health=100, score=0):
        self.name = name
        self.__health = health      # private
        self.__score = score        # private

    # --- წვდომა private ატრიბუტებზე ---
    @property
    def health(self):
        return self.__health

    @property
    def score(self):
        return self.__score

    @staticmethod
    def random_event():
        # შემთხვევითი მოვლენა. აბრუნებს (აღწერა, რა_იცვლება, რამდენით).
        return random.choice(Hero.EVENTS)

    @classmethod
    def from_name(cls, name):
        # ქმნის გმირს მხოლოდ სახელით, დანარჩენი default-ია.
        return cls(name)

    def apply_event(self, event):
        description, field, amount = event
        if field == "score":
            self.__score += amount
        else:
            self.__health += amount
            if self.__health < 0:
                self.__health = 0
        sign = "+" if amount > 0 else ""
        print(f"  {description} ({field} {sign}{amount})  "
              f"-> HP={self.__health}, ქულა={self.__score}")

    def is_alive(self):
        return self.__health > 0

    def __str__(self):
        return f"{self.name} | HP={self.__health} | ქულა={self.__score}"


class SuperHero(Hero):
    # დამატებითი ძალა — ამცირებს მიღებულ დაზიანებას.

    def __init__(self, name, power, health=100, score=0):
        super().__init__(name, health, score)   # მშობლის კონსტრუქტორი
        self.power = power

    @classmethod
    def from_name(cls, name, power="ფარი"):
        return cls(name, power)

    def apply_event(self, event):
        description, field, amount = event
        # სუპერგმირი დაზიანების ნახევარს იღებს
        if field == "health" and amount < 0:
            amount = amount // 2
            event = (f"{description} [{self.power} იცავს!]", field, amount)
        super().apply_event(event)              # მშობლის ლოგიკა


def play(hero, max_turns=15):
    print("=" * 60)
    print(f"თამაში იწყება: {hero}")
    print("=" * 60)

    turn = 1
    while hero.is_alive() and turn <= max_turns:
        print(f"\nსვლა {turn}:")
        hero.apply_event(Hero.random_event())
        turn += 1

    print("\n" + "-" * 60)
    if hero.is_alive():
        print(f"გმირი გადარჩა! საბოლოო: {hero}")
    else:
        print(f"გმირი დაეცა. საბოლოო ქულა: {hero.score}")
    print("-" * 60)


if __name__ == "__main__":
    random.seed(3)

    # ჩვეულებრივი გმირი — classmethod-ით შექმნილი
    hero = Hero.from_name("ლუკა")
    play(hero)

    print("\n")

    # სუპერგმირი — იგივე მოვლენები, მაგრამ ნახევარი დაზიანება
    random.seed(3)   # იგივე მოვლენები, რომ შედარება სამართლიანი იყოს
    superhero = SuperHero.from_name("ნიკა", power="ალმასის ჯავშანი")
    play(superhero)

    print("\n--- ენკაფსულაცია მუშაობს? ---")
    try:
        hero.__health = 9999
        print("hero.__health = 9999 ჩაიწერა, მაგრამ ნამდვილი health:", hero.health)
        print("(ეს უბრალოდ ახალი ატრიბუტი შეიქმნა, private-ს არ შეხებია)")
    except AttributeError as e:
        print("შეცდომა:", e)