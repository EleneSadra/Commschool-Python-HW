# დავალება #8 — ამოცანა 5: Temperature
# @property გვაძლევს საშუალებას მეთოდი გამოვიყენოთ ატრიბუტივით:
#  t.celsius        (და არა t.get_celsius())
#  t.celsius = 30   (და არა t.set_celsius(30))
# fahrenheit read-only-ია — მას მხოლოდ getter აქვს, setter არა.
# ამიტომ ის ყოველთვის __celsius-იდან ითვლება და ავტომატურად "ახლდება".


class Temperature:
    def __init__(self, celsius=0):
        self.__celsius = celsius

    # --- celsius: getter + setter ---
    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("აბსოლუტურ ნულზე დაბლა ტემპერატურა არ არსებობს.")
        self.__celsius = value

    # --- fahrenheit: მხოლოდ getter (read-only) ---
    @property
    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32

    def __str__(self):
        return f"{self.__celsius}°C = {self.fahrenheit}°F"


if __name__ == "__main__":
    t = Temperature(25)
    print(t)

    print("\n--- ვცვლით °C-ს და ვამოწმებთ, °F ავტომატურად იცვლება თუ არა ---")
    for c in [0, 37, 100, -40]:
        t.celsius = c
        print(f"celsius = {c:>5}  ->  fahrenheit = {t.fahrenheit}")

    # -40 საინტერესო წერტილია: ერთადერთი, სადაც °C და °F ემთხვევა

    print("\n--- fahrenheit read-only-ია ---")
    try:
        t.fahrenheit = 100
    except AttributeError as e:
        print("fahrenheit-ის შეცვლა აკრძალულია:", e)

    print("\n--- ვალიდაცია setter-ში ---")
    try:
        t.celsius = -500
    except ValueError as e:
        print("ValueError:", e)