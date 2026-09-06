# # დავალება #11 — ნაწილი 1: unittest
# ამოცანები #1, #2, #3

# ────────────────────────────────────────────────────────────────
# ფაილის სახელის შესახებ
# ────────────────────────────────────────────────────────────────
# პირობაში ეწერა "unittest.py". პატარა ასოებით ეს ფაილი ვერ იმუშავებს:
# როცა პითონი ხედავს `import unittest`, ის ჯერ იმავე საქაღალდეში ეძებს
# და თავის თავს იმპორტავს — შედეგად:

#     AttributeError: partially initialized module 'unittest'
#     has no attribute 'TestCase' (most likely due to a circular import)

# ამიტომ ფაილს ჰქვია "Unittest.py" — დიდი U-თი. Linux-ზე იმპორტები
# რეგისტრზეა დამოკიდებული, ამიტომ `import unittest` სტანდარტულ
# ბიბლიოთეკას პოულობს და არა ამ ფაილს.

# გაშვება:  python3 Unittest.py
# დეტალურად: python3 Unittest.py -v
# ────────────────────────────────────────────────────────────────

import unittest


# ══════════════════════════════════════════════════════════════
# ამოცანა #1 — Calculator
# ══════════════════════════════════════════════════════════════
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("0-ზე გაყოფა შეუძლებელია")
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        # setUp() ავტომატურად გაეშვება ყოველი ტესტის წინ.
        # ანუ ყოველი ტესტი ახალ, სუფთა Calculator-ს იღებს —
        # ერთი ტესტი ვერ იმოქმედებს მეორეზე.
        self.calc = Calculator()

    # --- Positive testing: სწორი მონაცემები ---
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333, places=6)

    # --- Negative testing: 0-ზე გაყოფა ---
    def test_divide_by_zero(self):
        # assertRaises ამოწმებს, რომ შეცდომა მართლა ამოვარდა.
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)


# ══════════════════════════════════════════════════════════════
# ამოცანა #2 — BankAccount
# ══════════════════════════════════════════════════════════════
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("შესატანი თანხა დადებითი უნდა იყოს")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("გასატანი თანხა დადებითი უნდა იყოს")
        if amount > self.balance:
            raise ValueError("ბალანსზე მეტი თანხის გატანა შეუძლებელია")
        self.balance -= amount
        return self.balance


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    # --- 1. სწორი ბალანსი ---
    def test_deposit_updates_balance(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_withdraw_updates_balance(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_multiple_operations(self):
        self.account.deposit(200)      # 300
        self.account.withdraw(50)      # 250
        self.account.deposit(25)       # 275
        self.assertEqual(self.account.balance, 275)

    # --- 2. უარყოფითი თანხის შეტანისას შეცდომა ---
    def test_negative_deposit_raises(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_zero_deposit_raises(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_balance_unchanged_after_failed_deposit(self):
        # შეცდომის შემდეგ ბალანსი არ უნდა შეიცვალოს.
        try:
            self.account.deposit(-50)
        except ValueError:
            pass
        self.assertEqual(self.account.balance, 100)

    # --- 3. ბალანსზე მეტის გატანისას შეცდომა ---
    def test_overdraw_raises(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(500)

    def test_overdraw_error_message(self):
        # assertRaises-ს context manager-ად ვიყენებთ, რომ ტექსტიც შევამოწმოთ.
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(500)
        self.assertIn("ბალანსზე მეტი", str(context.exception))

    def test_withdraw_exact_balance_works(self):
        # ზუსტად ბალანსის ოდენობის გატანა უნდა მუშაობდეს.
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 0)


# ══════════════════════════════════════════════════════════════
# ამოცანა #3 — JSON response-იდან status
# ══════════════════════════════════════════════════════════════
def get_status(response):
    
    # იღებს dict-ს და აბრუნებს "status"-ის მნიშვნელობას.
    # თუ status არ არსებობს — KeyError.

    if not isinstance(response, dict):
        raise TypeError("response უნდა იყოს dict")
    if "status" not in response:
        raise KeyError("პასუხში 'status' ველი არ არის")
    return response["status"]


class TestGetStatus(unittest.TestCase):
    def setUp(self):
        self.valid_response = {"status": "success", "code": 200}

    # --- Positive ---
    def test_returns_status(self):
        self.assertEqual(get_status(self.valid_response), "success")

    def test_returns_error_status(self):
        self.assertEqual(get_status({"status": "error"}), "error")

    def test_status_can_be_number(self):
        self.assertEqual(get_status({"status": 404}), 404)

    def test_status_can_be_none(self):
        # None ლეგიტიმური მნიშვნელობაა — ველი ხომ არსებობს.
        self.assertIsNone(get_status({"status": None}))

    # --- Negative ---
    def test_missing_status_raises(self):
        with self.assertRaises(KeyError):
            get_status({"code": 200, "message": "OK"})

    def test_empty_dict_raises(self):
        with self.assertRaises(KeyError):
            get_status({})

    def test_not_a_dict_raises(self):
        with self.assertRaises(TypeError):
            get_status("status: success")


if __name__ == "__main__":
    unittest.main(verbosity=2)