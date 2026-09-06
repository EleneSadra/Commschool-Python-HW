# დავალება #8 — ამოცანა 8: FunnyCalculator

# ყურადღება ერთ დეტალზე:
# პირობაში წერია `10 / calc` — აქ calc მარჯვნივ დგას, მარცხნივ კი int.
# პითონი ჯერ ცდილობს (10).__truediv__(calc)-ს, int-მა არ იცის რა ქნას
# FunnyCalculator-თან და აბრუნებს NotImplemented. მხოლოდ ამის შემდეგ
# პითონი ცდილობს calc.__rtruediv__(10)-ს — "reflected" ვერსიას.

# ამიტომ მხოლოდ __truediv__ საკმარისი არ არის: `10 / calc` მასთან
# TypeError-ს დააგდებდა. გვჭირდება __rtruediv__ იმისთვის, რომ
# პირობაში მოცემული `10 / calc` იმუშაოს.


class FunnyCalculator:
    def __add__(self, other):
        return "Why are you adding numbers? Just buy a calculator"

    def __mul__(self, other):
        return "Multiplication is too mainstream..."

    def __truediv__(self, other):
        # calc / რაღაც
        if other == 0:
            return "ZeroDivisionError? Nah, let's just say infinity"
        return "Division? In this economy?"

    def __rtruediv__(self, other):
        # რაღაც / calc  —  სწორედ ეს სჭირდება `10 / calc`-ს
        return "ZeroDivisionError? Nah, let's just say infinity"

    def __str__(self):
        return "I'm the funniest calculator in Python!"


if __name__ == "__main__":
    calc = FunnyCalculator()

    print("calc + 5  ->", calc + 5)
    print("calc * 2  ->", calc * 2)
    print("10 / calc ->", 10 / calc)      # __rtruediv__ იძახება
    print("calc / 0  ->", calc / 0)       # __truediv__, ნულზე გაყოფის შტო
    print("calc / 5  ->", calc / 5)       # __truediv__, ჩვეულებრივი შტო
    print("print(calc) ->", calc)         # __str__

    # დემონსტრაცია: რა მოხდებოდა __rtruediv__-ის გარეშე
    print("\n--- რატომ გვჭირდება __rtruediv__ ---")

    class BrokenCalculator:
        def __truediv__(self, other):
            return "მხოლოდ __truediv__ მაქვს"

    broken = BrokenCalculator()
    print("broken / 10 ->", broken / 10)   # მუშაობს
    try:
        print(10 / broken)
    except TypeError as e:
        print("10 / broken ->  TypeError:", e)