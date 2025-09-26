import pytest
from src.c_module import BankAccount, fibonacci, prime_factors, moving_average, normalize_scores

# C-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgnevad testid katavad klassi BankAccount ning kõik funktsioonid:
# - positiivsed ja negatiivsed juhtumid
# - servajuhtumid (edge cases)
# - invariandid (nt algne arv = toode algteguritest)

# -----------------------
# BankAccount testid
# -----------------------

def test_create_account_valid_and_default_balance():
    a = BankAccount("Alice")
    assert a.balance() == 0
    b = BankAccount("Bob", 100)
    assert b.balance() == 100

def test_create_account_invalid_owner_and_balance():
    with pytest.raises(ValueError):
        BankAccount("", 10)            # tühi string ei ole lubatud
    with pytest.raises(ValueError):
        BankAccount(123, 10)          # mitte-sõne ei ole lubatud
    with pytest.raises(ValueError):
        BankAccount("Eve", -1)        # negatiivne algsaldo ei ole lubatud

def test_deposit_accepts_positive_and_rejects_nonpositive():
    a = BankAccount("Alice", 10)
    a.deposit(15)
    assert a.balance() == 25

    with pytest.raises(ValueError):
        a.deposit(0)
    with pytest.raises(ValueError):
        a.deposit(-5)

def test_withdraw_valid_and_invalid():
    a = BankAccount("Bob", 50)
    a.withdraw(20)
    assert a.balance() == 30

    # täpne saldo välja võtta peaks õnnestuma ja jätta 0
    a.withdraw(30)
    assert a.balance() == 0

    with pytest.raises(ValueError):
        a.withdraw(1)   # liiga palju (saldo 0)
    with pytest.raises(ValueError):
        a.withdraw(0)
    with pytest.raises(ValueError):
        a.withdraw(-10)

def test_transfer_valid_and_invalid():
    a = BankAccount("Sender", 100)
    b = BankAccount("Receiver", 10)
    a.transfer_to(b, 40)
    assert a.balance() == 60
    assert b.balance() == 50

    # ülekandeks peab teine pool olema BankAccount
    with pytest.raises(ValueError):
        a.transfer_to("not an account", 10)
    # negatiivne või 0 summa keelatud
    with pytest.raises(ValueError):
        a.transfer_to(b, 0)
    with pytest.raises(ValueError):
        a.transfer_to(b, -5)
    # liiga suur summa keelatud
    with pytest.raises(ValueError):
        a.transfer_to(b, 1000)

def test_transfer_exact_balance_leaves_zero():
    a = BankAccount("X", 30)
    b = BankAccount("Y", 0)
    a.transfer_to(b, 30)
    assert a.balance() == 0
    assert b.balance() == 30

# -----------------------
# fibonacci testid
# -----------------------

def test_fibonacci_small():
    """Test Fibonacci arvude arvutamist (baasjuhtumid ja väikesed väärtused)."""
    assert [fibonacci(i) for i in range(6)] == [0, 1, 1, 2, 3, 5]
    assert fibonacci(10) == 55

def test_fibonacci_additional_values_and_negative():
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(7) == 13
    assert fibonacci(20) == 6765

    with pytest.raises(ValueError):
        fibonacci(-1)

# -----------------------
# prime_factors testid
# -----------------------

def test_prime_factors_basic_and_primes():
    assert prime_factors(2) == [2]
    assert prime_factors(3) == [3]
    assert prime_factors(4) == [2, 2]
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(97) == [97]

def test_prime_factors_composite_and_repeated():
    # 2^10 = 1024
    assert prime_factors(1024) == [2] * 10

    n = 2 * 3 * 5 * 7 * 11
    assert prime_factors(n) == [2, 3, 5, 7, 11]

def test_prime_factors_product_and_order():
    # kontrolli, et algtegurid korrutades annavad algse arvu ning on kasvavas järjekorras
    cases = [18, 360, 9973*2, 2*2*3*13]
    for x in cases:
        factors = prime_factors(x)
        prod = 1
        for f in factors:
            prod *= f
        assert prod == x
        assert factors == sorted(factors)

def test_prime_factors_invalid_inputs():
    with pytest.raises(ValueError):
        prime_factors(1)
    with pytest.raises(ValueError):
        prime_factors(0)
    with pytest.raises(ValueError):
        prime_factors(-10)

# -----------------------
# moving_average testid
# -----------------------

def test_moving_average_basic_and_window_equal_len():
    vals = [1, 2, 3, 4, 5]
    assert moving_average(vals, 3) == [2.0, 3.0, 4.0]

    vals2 = [10, 20, 30]
    assert moving_average(vals2, 3) == [20.0]

def test_moving_average_window_one_and_empty_list():
    vals = [4, 5, 6]
    # aken=1 peaks tagastama iga väärtuse float-ina
    res = moving_average(vals, 1)
    assert res == [4.0, 5.0, 6.0]
    assert all(isinstance(x, float) for x in res)

    # tühja listi puhul aken>0 -> tühi tulemus
    assert moving_average([], 1) == []

def test_moving_average_float_and_negative_values():
    vals = [1.5, -0.5, 2.0, 3.5]
    # akna 2 liikuv keskmine
    expected = [(1.5 + -0.5) / 2.0, (-0.5 + 2.0) / 2.0, (2.0 + 3.5) / 2.0]
    assert moving_average(vals, 2) == pytest.approx(expected)

def test_moving_average_invalid_window():
    with pytest.raises(ValueError):
        moving_average([1, 2, 3], 0)
    with pytest.raises(ValueError):
        moving_average([1, 2, 3], -1)

# -----------------------
# normalize_scores testid
# -----------------------

def test_normalize_scores_valid_boundaries_and_types():
    scores = [0, 50, 100]
    out = normalize_scores(scores)
    assert out == [0.0, 0.5, 1.0]
    assert all(isinstance(x, float) for x in out)
    # pikkus peaks jääma samaks
    assert len(out) == len(scores)

    # ka ujukomaga skoorid on lubatud
    scores2 = [33.3, 66.6]
    out2 = normalize_scores(scores2)
    assert out2 == pytest.approx([0.333, 0.666], rel=1e-3)

def test_normalize_scores_invalid_values():
    with pytest.raises(ValueError):
        normalize_scores([-0.1, 50])
    with pytest.raises(ValueError):
        normalize_scores([10, 100.1])

def test_normalize_scores_non_numeric_raises():
    # kui sisestada mittenumerable või mittesobivad tüübid, võib tekkida TypeError/ValueError
    with pytest.raises((TypeError, ValueError)):
        normalize_scores(["a", 50])
