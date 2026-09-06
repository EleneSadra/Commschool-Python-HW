# დავალება #8 — ამოცანა 3: @dataclass Book
# @dataclass ავტომატურად გვიწერს __init__, __repr__ და __eq__ მეთოდებს.
# ჩვენ მხოლოდ ველების ტიპებს ვწერთ.


from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int

    def is_classic(self):
        # აბრუნებს True, თუ წელი < 1970.
        return self.year < 1970


if __name__ == "__main__":
    books = [
        Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 1189),
        Book("დიდოსტატის მარჯვენა", "კონსტანტინე გამსახურდია", 1939),
        Book("1984", "George Orwell", 1949),
        Book("Harry Potter", "J.K. Rowling", 1997),
        Book("Clean Code", "Robert Martin", 2008),
    ]

    for b in books:
        status = "კლასიკაა" if b.is_classic() else "თანამედროვეა"
        print(f"{b.title:<28} ({b.year}) -> {status}")

    # @dataclass-ის უფასო ბონუსები:
    print("\n__repr__ უფასოდ:", books[2])
    print("__eq__ უფასოდ:", Book("1984", "George Orwell", 1949) == books[2])