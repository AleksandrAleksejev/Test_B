import pytest
from src.c_module import BankAccount, fibonacci, prime_factors, moving_average, normalize_scores

# C-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_fibonacci_small():
    """Test Fibonacci arvude arvutamist."""
    assert [fibonacci(i) for i in range(6)] == [0,1,1,2,3,5]
    assert fibonacci(10) == 55

def test_prime_factors_basic():
    """Test algtegurite leidmist."""
    assert prime_factors(12) == [2,2,3]
    assert prime_factors(97) == [97]

# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!
