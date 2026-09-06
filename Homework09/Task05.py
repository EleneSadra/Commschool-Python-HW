# დავალება #9 — ამოცანა 5: პროგრამა კარტზე

# Card  — rank, suit
# Deck  — private cards list (__cards)
#         classmethod  create_standard_deck() -> სტანდარტული 52 კარტი
#         staticmethod shuffle(cards)         -> ურევს კარტებს

# განსხვავება, რომელიც ამ ამოცანაში კარგად ჩანს:
#   classmethod  იღებს cls-ს -> შეუძლია ახალი Deck შექმნას
#   staticmethod არაფერს იღებს -> უბრალოდ ამუშავებს გადაცემულ სიას

import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♠", "♥", "♦", "♣"]

    def __init__(self, cards=None):
        self.__cards = cards if cards is not None else []   # private

    @property
    def cards(self):
        # read-only წვდომა — გარედან სიის შეცვლა არ შეიძლება.
        return list(self.__cards)

    @classmethod
    def create_standard_deck(cls):
        # 13 rank × 4 suit = 52 კარტი.
        cards = [Card(rank, suit) for suit in cls.SUITS for rank in cls.RANKS]
        return cls(cards)

    @staticmethod
    def shuffle(cards):
        # ურევს გადაცემულ სიას. არ სჭირდება არც self, არც cls.
        shuffled = list(cards)
        random.shuffle(shuffled)
        return shuffled

    def shuffle_self(self):
        self.__cards = Deck.shuffle(self.__cards)

    def draw(self, count):
        """იღებს count კარტს დასტის თავიდან."""
        if count > len(self.__cards):
            raise ValueError("დასტაში საკმარისი კარტი არაა")
        drawn = self.__cards[:count]
        self.__cards = self.__cards[count:]
        return drawn

    def __len__(self):
        return len(self.__cards)


def check_simple_combination(hand):
    # ამოწმებს "მარტივ კომბინაციას" — არის თუ არა ორი ერთნაირი rank.
    # აბრუნებს (True/False, აღწერა).
    counts = {}
    for card in hand:
        counts[card.rank] = counts.get(card.rank, 0) + 1

    pairs = [rank for rank, n in counts.items() if n >= 2]
    if pairs:
        return True, f"ორი ერთნაირი: {', '.join(pairs)}"
    return False, "კომბინაცია არ არის"


if __name__ == "__main__":
    random.seed(11)

    deck = Deck.create_standard_deck()
    print(f"დასტა შეიქმნა: {len(deck)} კარტი")
    print("პირველი 13:", deck.cards[:13])

    deck.shuffle_self()
    print("\nარევის შემდეგ, პირველი 13:", deck.cards[:13])

    print("\n--- მოთამაშე იღებს 5 კარტს ---")
    hand = deck.draw(5)
    print("ხელი:", hand)

    has_combo, description = check_simple_combination(hand)
    print("შედეგი:", description)
    print(f"დასტაში დარჩა: {len(deck)} კარტი")

    # რამდენიმე დარიგება — რომ კომბინაციიანი ხელიც დავინახოთ
    print("\n--- კიდევ 5 დარიგება ---")
    for i in range(1, 6):
        if len(deck) < 5:
            break
        hand = deck.draw(5)
        has_combo, description = check_simple_combination(hand)
        mark = "✅" if has_combo else "  "
        print(f"  {mark} {str(hand):<32} {description}")

    print("\n--- private cards დაცულია? ---")
    d = Deck.create_standard_deck()
    try:
        print(d.__cards)
    except AttributeError as e:
        print("პირდაპირი წვდომა ვერ ხერხდება:", e)
    d.cards.clear()          # ასლს ვასუფთავებთ, ორიგინალს არა
    print("cards.clear()-ის შემდეგ დასტაშია:", len(d), "კარტი")