import pytest
from tests.test_c_module import BankAccount, fibonacci, prime_factors, moving_average, normalize_scores

# --- Testid BankAccount klassile ---

def test_create_account_valid():
    acc = BankAccount("Alice", 100)
    assert acc.balance() == 100

def test_create_account_invalid_owner():
    with pytest.raises(ValueError):
        BankAccount("", 50)
    with pytest.raises(ValueError):
        BankAccount(123, 50)

def test_create_account_negative_balance():
    with pytest.raises(ValueError):
        BankAccount("Bob", -10)

def test_deposit_valid():
    acc = BankAccount("Alice", 0)
    acc.deposit(50)
    assert acc.balance() == 50

def test_deposit_invalid():
    acc = BankAccount("Alice", 10)
    with pytest.raises(ValueError):
        acc.deposit(0)
    with pytest.raises(ValueError):
        acc.deposit(-5)

def test_withdraw_valid():
    acc = BankAccount("Alice", 100)
    acc.withdraw(40)
    assert acc.balance() == 60

def test_withdraw_invalid():
    acc = BankAccount("Alice", 20)
    with pytest.raises(ValueError):
        acc.withdraw(0)
    with pytest.raises(ValueError):
        acc.withdraw(-5)
    with pytest.raises(ValueError):
        acc.withdraw(50)  # rohkem kui saldo

def test_transfer_valid():
    acc1 = BankAccount("Alice", 100)
    acc2 = BankAccount("Bob", 50)
    acc1.transfer_to(acc2, 30)
    assert acc1.balance() == 70
    assert acc2.balance() == 80

def test_transfer_invalid():
    acc1 = BankAccount("Alice", 10)
    acc2 = BankAccount("Bob", 0)
    with pytest.raises(ValueError):
        acc1.transfer_to("not_account", 5)
    with pytest.raises(ValueError):
        acc1.transfer_to(acc2, -5)
    with pytest.raises(ValueError):
        acc1.transfer_to(acc2, 20)  # liiga palju

# --- Testid fibonacci funktsioonile ---

def test_fibonacci_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_values():
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)

# --- Testid prime_factors funktsioonile ---

def test_prime_factors_small():
    assert prime_factors(2) == [2]
    assert prime_factors(3) == [3]
    assert prime_factors(4) == [2, 2]
    assert prime_factors(12) == [2, 2, 3]

def test_prime_factors_large_prime():
    assert prime_factors(29) == [29]

def test_prime_factors_invalid():
    with pytest.raises(ValueError):
        prime_factors(1)
    with pytest.raises(ValueError):
        prime_factors(0)

# --- Testid moving_average funktsioonile ---

def test_moving_average_basic():
    vals = [1, 2, 3, 4, 5]
    assert moving_average(vals, 3) == [2.0, 3.0, 4.0]

def test_moving_average_window_equals_len():
    vals = [10, 20, 30]
    assert moving_average(vals, 3) == [20.0]

def test_moving_average_large_window():
    vals = [1, 2]
    assert moving_average(vals, 3) == []

def test_moving_average_invalid_window():
    with pytest.raises(ValueError):
        moving_average([1, 2, 3], 0)

# --- Testid normalize_scores funktsioonile ---

def test_normalize_scores_valid():
    assert normalize_scores([0, 50, 100]) == [0.0, 0.5, 1.0]

def test_normalize_scores_invalid():
    with pytest.raises(ValueError):
        normalize_scores([-1, 50])
    with pytest.raises(ValueError):
        normalize_scores([10, 110])
