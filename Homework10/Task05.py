# დავალება #10 — ამოცანა 5: ტრანსპორტირების სისტემა

# - ყველა ტრანსპორტს აქვს fuel, speed, capacity
# - move() აბსტრაქტული მეთოდია
# - ყოველი ტრანსპორტი სხვადასხვა წესით ხარჯავს საწვავს (პოლიმორფიზმი)
# - fuel private-ია (ენკაფსულაცია)
# - ყველა ძირითად ფუნქციონალს Transport-იდან იღებს (მემკვიდრეობა)

# საწვავის ხარჯვის განსხვავებული წესები:
#   Car  — მანძილზე პროპორციული
#   Bus  — მანძილი + ჩამჯდარი მგზავრების რაოდენობა (რაც მეტია, მით მეტი)
#   Bike — საწვავს არ ხარჯავს (მძღოლის ენერგიაზე მუშაობს)

from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, name, fuel, speed, capacity):
        self.name = name
        self.__fuel = fuel          # private — ენკაფსულაცია
        self.speed = speed
        self.capacity = capacity
        self.passengers = 0

    # --- კონტროლირებადი წვდომა private საწვავზე ---
    @property
    def fuel(self):
        return self.__fuel

    def refuel(self, amount):
        if amount <= 0:
            raise ValueError("საწვავი დადებითი უნდა იყოს")
        self.__fuel += amount
        print(f"  ⛽ {self.name}: დაემატა {amount}. საწვავი: {self.__fuel:.1f}")

    def _burn(self, amount):
        # protected — მხოლოდ შვილები იყენებენ move()-ის შიგნით.
        if amount > self.__fuel:
            return False
        self.__fuel -= amount
        return True

    def board(self, count):
        if self.passengers + count > self.capacity:
            print(f"  ❌ {self.name}: ადგილი არ არის "
                  f"({self.passengers}/{self.capacity})")
            return
        self.passengers += count
        print(f"  🧍 {self.name}: ჩაჯდა {count}. "
              f"სულ: {self.passengers}/{self.capacity}")

    # --- აბსტრაქტული: ყველა შვილი ვალდებულია დაწეროს ---
    @abstractmethod
    def move(self, distance):
        pass

    @abstractmethod
    def fuel_needed(self, distance):
        # რამდენი საწვავი დასჭირდება — თითოეულს თავისი ფორმულა
        pass

    def __str__(self):
        return (f"{self.name} ({type(self).__name__}) | "
                f"საწვავი: {self.fuel:.1f} | სიჩქარე: {self.speed} კმ/სთ | "
                f"ადგილები: {self.capacity}")


class Car(Transport):
    def fuel_needed(self, distance):
        return distance * 0.08          # 8 ლიტრი 100 კმ-ზე

    def move(self, distance):
        needed = self.fuel_needed(distance)
        if not self._burn(needed):
            print(f"  ❌ {self.name}: საწვავი არ ჰყოფნის "
                  f"({self.fuel:.1f} < {needed:.1f})")
            return
        time = distance / self.speed
        print(f"  🚗 {self.name}: გაიარა {distance} კმ {time:.1f} სთ-ში, "
              f"დახარჯა {needed:.1f}. დარჩა: {self.fuel:.1f}")


class Bus(Transport):
    def fuel_needed(self, distance):
        # ბაზა + დამატება ყოველ მგზავრზე
        return distance * 0.25 + self.passengers * distance * 0.005

    def move(self, distance):
        needed = self.fuel_needed(distance)
        if not self._burn(needed):
            print(f"  ❌ {self.name}: საწვავი არ ჰყოფნის "
                  f"({self.fuel:.1f} < {needed:.1f})")
            return
        time = distance / self.speed
        print(f"  🚌 {self.name}: გაიარა {distance} კმ {time:.1f} სთ-ში "
              f"{self.passengers} მგზავრით, დახარჯა {needed:.1f}. "
              f"დარჩა: {self.fuel:.1f}")


class Bike(Transport):
    def fuel_needed(self, distance):
        return 0                        # საწვავს არ ხარჯავს

    def move(self, distance):
        self._burn(0)
        time = distance / self.speed
        print(f"  🚲 {self.name}: გაიარა {distance} კმ {time:.1f} სთ-ში. "
              f"საწვავი არ დაუხარჯავს (მძღოლის ენერგია).")


if __name__ == "__main__":
    fleet = [
        Car("Toyota", fuel=45, speed=90, capacity=5),
        Bus("ავტობუსი #338", fuel=120, speed=50, capacity=40),
        Bike("ველოსიპედი", fuel=0, speed=18, capacity=1),
    ]

    print("=" * 70)
    print("პარკი")
    print("=" * 70)
    for t in fleet:
        print("  ", t)

    print("\n" + "=" * 70)
    print("მგზავრების ჩასხდომა")
    print("=" * 70)
    fleet[0].board(3)
    fleet[1].board(25)
    fleet[2].board(1)
    fleet[1].board(20)          # ადგილი აღარაა

    print("\n" + "=" * 70)
    print("პოლიმორფიზმი — ერთი ციკლი, სამი განსხვავებული move()")
    print("=" * 70)
    for t in fleet:
        t.move(100)

    print("\n" + "=" * 70)
    print("იგივე მანძილი, განსხვავებული ხარჯი")
    print("=" * 70)
    for t in fleet:
        print(f"  {type(t).__name__:<6} 100 კმ-ზე: "
              f"{t.fuel_needed(100):.1f} ერთეული საწვავი")

    print("\n" + "=" * 70)
    print("ენკაფსულაცია და აბსტრაქცია")
    print("=" * 70)

    car = fleet[0]
    try:
        print(car.__fuel)
    except AttributeError as e:
        print("   private fuel-ზე პირდაპირი წვდომა:", e)

    car.refuel(20)

    try:
        Transport("ზოგადი", 10, 10, 1)
    except TypeError as e:
        print("   Transport-ის შექმნა:", e)