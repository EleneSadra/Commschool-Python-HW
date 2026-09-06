# დავალება #11 — ნაწილი 2: pytest
# ამოცანები #4, #5, #6

# ────────────────────────────────────────────────────────────────
# ფაილის სახელის შესახებ
# ────────────────────────────────────────────────────────────────
# პირობაში ეწერა "pytest.py". პატარა ასოებით `import pytest` თავის
# თავს იმპორტავდა და ტესტები ვერ გაეშვებოდა. ამიტომ — "pytest.py".

# გაშვება:  python3 -m pytest pytest.py -v

# შენიშვნა: ლექციაზე იყო ნათქვამი, რომ pytest ავტომატურად პოულობს
# ფაილებს, რომლებიც `test_`-ით იწყება ან `_test.py`-ით მთავრდება.
# "pytest.py" არცერთს არ შეესაბამება, ამიტომ ფაილის სახელი ხელით
# უნდა მივუთითოთ (როგორც ზემოთ). თუ გინდა, რომ უბრალო `pytest`
# ბრძანებამაც იპოვოს, ფაილს დაარქვი `test_pytest.py`.
# ────────────────────────────────────────────────────────────────

import pytest


# ══════════════════════════════════════════════════════════════
# ამოცანა #4 — Celsius → Fahrenheit (pytest.approx)
# ══════════════════════════════════════════════════════════════
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def test_freezing_point():
    assert celsius_to_fahrenheit(0) == pytest.approx(32.0)


def test_boiling_point():
    assert celsius_to_fahrenheit(100) == pytest.approx(212.0)


def test_body_temperature():
    assert celsius_to_fahrenheit(37) == pytest.approx(98.6)


def test_negative_temperature():
    """-40 ერთადერთი წერტილია, სადაც °C და °F ემთხვევა."""
    assert celsius_to_fahrenheit(-40) == pytest.approx(-40.0)


def test_decimal_value():
    assert celsius_to_fahrenheit(36.6) == pytest.approx(97.88)


def test_why_approx_is_needed():
    """
    რატომ approx და არა ==?

    float-ები ორობით სისტემაში ზუსტად არ ინახება.
    36.6°C -> 97.88 უნდა იყოს, მაგრამ პითონი 97.88000000000001-ს იღებს,
    ამიტომ `== 97.88` ჩავარდებოდა. approx ამოწმებს
    "საკმარისად ახლოს არის თუ არა" და არა "ზუსტად ტოლია თუ არა".

    (ყველა რიცხვს ეს პრობლემა არ აქვს — მაგ. 37°C ზუსტად 98.6-ს იძლევა.
     სწორედ ამიტომ არის approx უსაფრთხო არჩევანი: არ გვჭირდება წინასწარ
     ვიცოდეთ, რომელ რიცხვზე გაჩნდება ცდომილება.)
    """
    result = celsius_to_fahrenheit(36.6)
    assert result == 97.88000000000001       # ასე ინახება სინამდვილეში
    assert result != 97.88                   # ზუსტად ტოლი არ არის!
    assert result == pytest.approx(97.88)    # მაგრამ approx-ით ტოლია


def test_approx_with_tolerance():
    """rel-ით შეგვიძლია ბუნდოვანების ზღვარი თვითონ დავაწესოთ."""
    assert celsius_to_fahrenheit(25) == pytest.approx(77, rel=1e-3)


# ══════════════════════════════════════════════════════════════
# ამოცანა #5 — ლოგინის შემოწმება (pytest.raises)
# ══════════════════════════════════════════════════════════════
USERS = {
    "elene": "pass123",
    "admin": "admin1234",
    "beka": "python2024",
}


def login(username, password):
    """
    ამოწმებს მომხმარებელს და პაროლს.
    არასწორი მონაცემები -> ValueError
    """
    if not username or not password:
        raise ValueError("მომხმარებელი და პაროლი ცარიელი არ უნდა იყოს")
    if username not in USERS:
        raise ValueError(f"მომხმარებელი '{username}' ვერ მოიძებნა")
    if USERS[username] != password:
        raise ValueError("პაროლი არასწორია")
    return True


# --- Positive ---
def test_valid_login():
    assert login("elene", "pass123") is True


def test_valid_login_admin():
    assert login("admin", "admin1234") is True


# --- Negative: pytest.raises ---
def test_wrong_password_raises():
    with pytest.raises(ValueError):
        login("elene", "wrongpassword")


def test_unknown_user_raises():
    with pytest.raises(ValueError):
        login("davit", "pass123")


def test_empty_username_raises():
    with pytest.raises(ValueError):
        login("", "pass123")


def test_empty_password_raises():
    with pytest.raises(ValueError):
        login("elene", "")


def test_error_message_for_wrong_password():
    """match-ით შეგვიძლია შეცდომის ტექსტიც შევამოწმოთ."""
    with pytest.raises(ValueError, match="პაროლი არასწორია"):
        login("elene", "12345")


def test_error_message_for_unknown_user():
    with pytest.raises(ValueError) as exc_info:
        login("nonexistent", "pass")
    assert "ვერ მოიძებნა" in str(exc_info.value)


# ══════════════════════════════════════════════════════════════
# ამოცანა #6 — email-ის ვალიდაცია (parametrize)
# ══════════════════════════════════════════════════════════════
def is_valid_email(text):
    """
    სწორი email შეიცავს @-ს და .-ს (პირობის მიხედვით).
    დამატებით: @ უნდა იყოს . -ზე ადრე და ცარიელი ნაწილები არ უნდა იყოს.
    """
    if not isinstance(text, str):
        return False
    if "@" not in text or "." not in text:
        return False
    if text.count("@") != 1:
        return False

    local, domain = text.split("@")
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    return True


@pytest.mark.parametrize("email", [
    "elene@gmail.com",
    "test.user@example.org",
    "a@b.co",
    "student@freeuni.edu.ge",
    "info@pavebank.ge",
])
def test_valid_emails(email):
    """
    parametrize ერთ ტესტს ბევრჯერ უშვებს — თითო მნიშვნელობაზე ერთხელ.
    შედეგში 5 ცალკე ტესტს დაინახავ და არა ერთს.
    """
    assert is_valid_email(email) is True


@pytest.mark.parametrize("email", [
    "elenegmail.com",       # @ არ არის
    "elene@gmailcom",       # . არ არის დომენში
    "elene@@gmail.com",     # ორი @
    "@gmail.com",           # ცარიელი local ნაწილი
    "elene@",               # ცარიელი დომენი
    "elene@.com",           # დომენი წერტილით იწყება
    "elene@gmail.",         # დომენი წერტილით მთავრდება
    "",                     # ცარიელი სტრიქონი
    "უბრალო ტექსტი",        # საერთოდ არაა email
])
def test_invalid_emails(email):
    assert is_valid_email(email) is False


@pytest.mark.parametrize("email,expected", [
    ("elene@gmail.com", True),
    ("test@freeuni.edu.ge", True),
    ("no-at-sign.com", False),
    ("no-dot@domain", False),
    ("", False),
])
def test_emails_with_expected_result(email, expected):
    """ორი პარამეტრის ვარიანტი — შესატანი და მოსალოდნელი შედეგი ერთად."""
    assert is_valid_email(email) is expected


@pytest.mark.parametrize("value", [None, 123, [], {}, True])
def test_non_string_input(value):
    """არა-სტრიქონი ყოველთვის False უნდა იყოს და არ უნდა ჩამოვარდეს."""
    assert is_valid_email(value) is False