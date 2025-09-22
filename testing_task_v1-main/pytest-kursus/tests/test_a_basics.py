import math
import pytest
from src.a_basics import (
    add, sub, mul, div, sum_list, is_even, factorial, reverse_string,
    is_palindrome, to_title_case, clamp, median, unique_letters, safe_int, nth_root
)

# A-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_add_basic():
    """Test liitmise funktsiooni."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_sub_basic():
    """Test lahutamise funktsiooni."""
    assert sub(10, 7) == 3
    assert sub(5, 3) == 2
    assert sub(0, 5) == -5


def test_mul_basic_and_zero():
    assert mul(3, 4) == 12
    assert mul(8, 0) == 0
    assert mul(-2, 5) == -10


def test_div_basic_and_zero_error():
    assert div(9, 3) == 3
    assert div(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


def test_sum_list_empty_and_values():
    assert sum_list([]) == 0
    assert sum_list([1, 2, 3, 4]) == 10
    assert sum_list([-2, 2, -3, 3]) == 0


def test_is_even_true_false():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True


def test_factorial_base_and_values_and_error():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)


def test_reverse_string_basic():
    assert reverse_string("Tere") == "ereT"
    assert reverse_string("") == ""


def test_is_palindrome_spaces_and_case():
    assert is_palindrome("A santa at NASA") is True
    assert is_palindrome("Python") is False
    assert is_palindrome("kazak") is True


def test_to_title_case_basic():
    assert to_title_case("tere tulemast koju") == "Tere Tulemast Koju"
    assert to_title_case("üks-kaheksA üheksa") == "Üks-Kaheksa Üheksa"


def test_clamp_inside_below_above():
    assert clamp(5, 1, 10) == 5
    assert clamp(-3, 0, 5) == 0
    assert clamp(99, 0, 5) == 5


def test_median_odd_even_and_empty_error():
    assert median([1, 5, 3]) == 3
    assert median([1, 2, 3, 4]) == 2.5
    with pytest.raises(ValueError):
        median([])


def test_unique_letters_basic():
    out = unique_letters("AaBb!! cc")
    assert out == {"a", "b", "c"}


def test_safe_int_ok_and_default():
    assert safe_int("42") == 42
    assert safe_int("x", default=-1) == -1
    assert safe_int(" 7 ") == 7


def test_nth_root_square_cube_and_errors():
    assert pytest.approx(nth_root(9, 2), rel=1e-6) == 3.0
    assert pytest.approx(nth_root(27, 3), rel=1e-6) == 3.0
    with pytest.raises(ValueError):
        nth_root(10, 0)
    with pytest.raises(ValueError):
        nth_root(-1, 2)
