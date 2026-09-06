# დავალება #10 — ამოცანა 3: Earth კლასი და OOP-ის 4 პრინციპი

# ლოგიკური თანმიმდევრობა დაცულია: ყველა კლასი დედამიწის ბუნებრივი
# სისტემაა. არსად არ ვინახავთ სხვა კატეგორიის ობიექტს (მაგალითად,
# Ocean-ში Engine-ს) — სწორედ ამაზე იყო გაფრთხილება პირობაში.

# --- სად რომელი პრინციპია ---

# 1. აბსტრაქცია (Abstraction)
#    Earth არის ABC. მასში @abstractmethod describe() და climate_effect().
#    Earth-ის პირდაპირ შექმნა შეუძლებელია — ის მხოლოდ "კონტრაქტია".

# 2. ენკაფსულაცია (Encapsulation)
#    __area_km2 და __temperature private-ია. გარედან წვდომა მხოლოდ
#    property-ითა და heat()/cool() მეთოდებით, რომლებიც წესებს ამოწმებენ.

# 3. მემკვიდრეობა (Inheritance)
#    Ocean, Forest, Desert — სამივე Earth-ის შვილია და იღებს
#    საერთო ფუნქციონალს (location(), area, temperature).

# 4. პოლიმორფიზმი (Polymorphism)
#    describe() და climate_effect() სამივე შვილში სხვადასხვაგვარად
#    მუშაობს. ერთი ციკლი — სამი განსხვავებული ქცევა.

# 5. მრავალჯერადი მემკვიდრეობა (Multiple Inheritance)
#    WaterSource და CarbonSink დამატებითი უნარებია (mixin).
#    Ocean(Earth, WaterSource), Forest(Earth, CarbonSink).

from abc import ABC, abstractmethod


# ─────────────── აბსტრაქტული მშობელი ───────────────
class Earth(ABC):
    planet = "Earth"                      # კლასის ატრიბუტი — ყველასთვის საერთო

    def __init__(self, name, area_km2, temperature):
        self.name = name
        self.__area_km2 = area_km2        # private — ენკაფსულაცია
        self.__temperature = temperature  # private

    # --- ენკაფსულაცია: კონტროლირებადი წვდომა ---
    @property
    def area_km2(self):
        return self.__area_km2

    @property
    def temperature(self):
        return self.__temperature

    def heat(self, degrees):
        if degrees <= 0:
            raise ValueError("გათბობა დადებითი უნდა იყოს")
        self.__temperature += degrees

    def cool(self, degrees):
        if degrees <= 0:
            raise ValueError("გაგრილება დადებითი უნდა იყოს")
        self.__temperature -= degrees

    # --- საერთო ლოგიკა, რომელსაც ყველა შვილი იღებს ---
    def location(self):
        return f"{self.name} მდებარეობს პლანეტაზე {self.planet}"

    # --- აბსტრაქცია: შვილები ვალდებულნი არიან ეს დაწერონ ---
    @abstractmethod
    def describe(self):
        pass

    @abstractmethod
    def climate_effect(self):
        pass

    def __str__(self):
        return f"{self.name} ({type(self).__name__}) | {self.area_km2:,} კმ² | {self.temperature}°C"


# ─────────────── Mixin კლასები (მრავალჯერადი მემკვიდრეობისთვის) ───────────────
class WaterSource:
    # უნარი: წყლის მიწოდება

    def provide_water(self):
        return f"{self.name} ამარაგებს წყლით"


class CarbonSink:
    # უნარი: ნახშირორჟანგის შთანთქმა.

    def absorb_co2(self):
        return f"{self.name} შთანთქავს CO₂-ს"


# ─────────────── შვილობილი კლასები ───────────────
class Ocean(Earth, WaterSource):
    def __init__(self, name, area_km2, temperature, depth_m):
        super().__init__(name, area_km2, temperature)
        self.depth_m = depth_m

    def describe(self):                      # პოლიმორფიზმი
        return f"{self.name} — ოკეანე, სიღრმე {self.depth_m} მ"

    def climate_effect(self):                # პოლიმორფიზმი
        return "ინახავს სითბოს და არეგულირებს ჰაერის ტემპერატურას"


class Forest(Earth, CarbonSink):
    def __init__(self, name, area_km2, temperature, tree_count):
        super().__init__(name, area_km2, temperature)
        self.tree_count = tree_count

    def describe(self):
        return f"{self.name} — ტყე, {self.tree_count:,} ხე"

    def climate_effect(self):
        return "გამოიმუშავებს ჟანგბადს და ამცირებს CO₂-ს"


class Desert(Earth):
    def __init__(self, name, area_km2, temperature, rainfall_mm):
        super().__init__(name, area_km2, temperature)
        self.rainfall_mm = rainfall_mm

    def describe(self):
        return f"{self.name} — უდაბნო, ნალექი წელიწადში {self.rainfall_mm} მმ"

    def climate_effect(self):
        return "ირეკლავს მზის სხივებს და ქმნის ცხელ ჰაერის ნაკადებს"


if __name__ == "__main__":
    systems = [
        Ocean("წყნარი ოკეანე", 165_250_000, 17, depth_m=4280),
        Forest("ამაზონის ტყე", 5_500_000, 26, tree_count=390_000_000),
        Desert("საჰარა", 9_200_000, 38, rainfall_mm=25),
    ]

    print("=" * 65)
    print("1. აბსტრაქცია — Earth-ის პირდაპირ შექმნა შეუძლებელია")
    print("=" * 65)
    try:
        Earth("ტესტი", 100, 20)
    except TypeError as e:
        print("  TypeError:", e)

    print("\n" + "=" * 65)
    print("2. პოლიმორფიზმი — ერთი ციკლი, სამი განსხვავებული ქცევა")
    print("=" * 65)
    for s in systems:
        print(f"\n  {s}")
        print(f"    describe()       -> {s.describe()}")
        print(f"    climate_effect() -> {s.climate_effect()}")

    print("\n" + "=" * 65)
    print("3. მემკვიდრეობა — location() მშობლიდან მოდის")
    print("=" * 65)
    for s in systems:
        print("  ", s.location())

    print("\n" + "=" * 65)
    print("4. მრავალჯერადი მემკვიდრეობა — mixin-ების უნარები")
    print("=" * 65)
    ocean, forest, desert = systems
    print("  ", ocean.provide_water())      # WaterSource-იდან
    print("  ", forest.absorb_co2())        # CarbonSink-იდან
    print("   Desert-ს არცერთი mixin არ აქვს:",
          hasattr(desert, "provide_water"), hasattr(desert, "absorb_co2"))

    print("\n   MRO — რა თანმიმდევრობით ეძებს პითონი მეთოდებს:")
    for cls in [Ocean, Forest, Desert]:
        chain = " -> ".join(c.__name__ for c in cls.mro())
        print(f"     {cls.__name__:<8}: {chain}")

    print("\n" + "=" * 65)
    print("5. ენკაფსულაცია — private ატრიბუტები")
    print("=" * 65)
    print(f"   საჰარას ტემპერატურა: {desert.temperature}°C")
    desert.heat(5)
    print(f"   heat(5)-ის შემდეგ:   {desert.temperature}°C")

    try:
        print(desert.__temperature)
    except AttributeError as e:
        print("   პირდაპირი წვდომა ვერ ხერხდება:", e)

    try:
        desert.heat(-10)
    except ValueError as e:
        print("   heat(-10) -> ValueError:", e)