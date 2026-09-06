# დავალება #9 — ამოცანა 3: მარტივი კაზინო თამაში
# staticmethod — არ სჭირდება არც self, არც cls. უბრალოდ ფუნქციაა,
#                რომელიც კლასის შიგნით ცხოვრობს, რადგან აზრობრივად იქ ეკუთვნის.
# classmethod   — იღებს cls-ს და ქმნის ობიექტს (factory).

import random


class SlotMachine:
    DIFFICULTY = {
        "easy":   ["🍒", "🍋", "🔔"],                      # 3 სიმბოლო
        "medium": ["🍒", "🍋", "🔔", "⭐", "💎"],           # 5 სიმბოლო
        "hard":   ["🍒", "🍋", "🔔", "⭐", "💎", "7️⃣", "🍀"],  # 7 სიმბოლო
    }

    def __init__(self, symbols, level="custom"):
        self.symbols = symbols
        self.level = level

    @staticmethod
    def generate_symbols(symbols, count=3):
        # შემთხვევითი სიმბოლოების გენერაცია. არ სჭირდება self და cls.
        return [random.choice(symbols) for _ in range(count)]

    @classmethod
    def from_difficulty(cls, level):
        # რაც უფრო რთულია დონე, მით მეტი სიმბოლოა — მოგება უფრო რთულია.
        if level not in cls.DIFFICULTY:
            raise ValueError(f"დონე უნდა იყოს: {list(cls.DIFFICULTY)}")
        return cls(cls.DIFFICULTY[level], level)

    def spin(self):
        # ერთი დატრიალება. მოგება — თუ სამივე სიმბოლო დაემთხვა.
        result = self.generate_symbols(self.symbols)
        won = result[0] == result[1] == result[2]
        return result, won

    def win_probability(self):
        # მოგების ალბათობა: 1 / (სიმბოლოების რაოდენობა ^ 2)
        return 1 / (len(self.symbols) ** 2)


if __name__ == "__main__":
    random.seed(7)

    for level in ["easy", "medium", "hard"]:
        machine = SlotMachine.from_difficulty(level)
        print("=" * 50)
        print(f"დონე: {level.upper()}  "
              f"({len(machine.symbols)} სიმბოლო, "
              f"მოგების შანსი: {machine.win_probability():.1%})")
        print("=" * 50)

        wins = 0
        spins = 10
        for i in range(1, spins + 1):
            result, won = machine.spin()
            status = "🎉 მოგება!" if won else "წაგება"
            if won:
                wins += 1
            print(f"  {i:>2}. {' | '.join(result)}   {status}")

        print(f"  შედეგი: {wins}/{spins} მოგება\n")

    # სტატისტიკური შემოწმება — ალბათობა თეორიას ემთხვევა თუ არა
    print("=" * 50)
    print("სტატისტიკა (10 000 დატრიალება თითო დონეზე)")
    print("=" * 50)
    for level in ["easy", "medium", "hard"]:
        machine = SlotMachine.from_difficulty(level)
        wins = sum(1 for _ in range(10_000) if machine.spin()[1])
        print(f"  {level:<7} ფაქტიური: {wins / 10_000:.2%}   "
              f"თეორიული: {machine.win_probability():.2%}")