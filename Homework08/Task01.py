# დავალება #8 - ამოცანა 1: BankAccount
# ენკაფსულაცია: __balance და __owner დახურული ატრიბუტებია.
# ერთი ქვედატირე  _x   -> protected. შეთანხმებაა: "გარედან ნუ შეეხები",
#                         მაგრამ ტექნიკურად წვდომა შესაძლებელია.
#                         მემკვიდრე კლასშიც თავისუფლად გამოიყენება.
# ორი ქვედატირე   __x  -> private. პითონი ჩართავს name mangling-ს:
#                         __balance გადაერქმევა _BankAccount__balance-ად,
#                         ამიტომ გარედან account.__balance აღარ მუშაობს.
# private ცვლადამდე მისასვლელად გვჭირდება getter და setter -
# ის დამხმარე ფუნქციები, რომლებიც ენკაფსულაციისას გამოიყენება.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        # თანხის დამატება.
        if amount <= 0:
            print("დეპოზიტი უნდა იყოს დადებითი რიცხვი.")
            return
        self.__balance += amount
        print(f"დაემატა {amount}. ბალანსი: {self.__balance}")

    def withdraw(self, amount):
        # თანხის გამოტანა - ბალანსი არ უნდა გადავიდეს მინუსში.
        if amount <= 0:
            print("გასატანი თანხა უნდა იყოს დადებითი რიცხვი.")
            return
        if amount > self.__balance:
            print(f"არასაკმარისი თანხა. ბალანსი: {self.__balance}, მოთხოვნა: {amount}")
            return
        self.__balance -= amount
        print(f"გატანილია {amount}. ბალანსი: {self.__balance}")

    def get_balance(self):
        # მხოლოდ წაკითხვისთვის — ერთადერთი ლეგალური გზა ბალანსის სანახავად.
        return self.__balance

    def get_owner(self):
        return self.__owner


if __name__ == "__main__":
    acc = BankAccount("ელენე", 100)

    acc.deposit(50)          # 150
    acc.withdraw(30)         # 120
    acc.withdraw(1000)       # უარი — არასაკმარისი თანხა
    acc.deposit(-10)         # უარი — უარყოფითი დეპოზიტი

    print("ბალანსი get_balance()-ით:", acc.get_balance())
    print("მფლობელი:", acc.get_owner())

    # ვამტკიცებთ, რომ პირდაპირი წვდომა არ მუშაობს:
    try:
        print(acc.__balance)
    except AttributeError as e:
        print("პირდაპირი წვდომა __balance-ზე ვერ ხერხდება:", e)

    # name mangling-ის დემონსტრაცია (ეს მუშაობს, მაგრამ ესეც "ჰაკია"):
    print("name mangling-ით:", acc._BankAccount__balance)

    # _protected vs __private მემკვიდრეობისას
    print("\n--- ერთი ქვედატირე vs ორი ქვედატირე ---")

    class Base:
        def __init__(self):
            self._protected = "ერთი ქვედატირე"
            self.__private = "ორი ქვედატირე"

    class Child(Base):
        def show(self):
            print("  _protected მემკვიდრეში:", self._protected)   # მუშაობს
            try:
                print(self.__private)
            except AttributeError as e:
                print("  __private მემკვიდრეში ვერ ჩანს:", e)

    Child().show()