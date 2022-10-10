# egy unit test az egy függvény

from list_functions import *


def test_remove_all():
    # given: előkészít
    numbers = [1, 2, 3, 1, 2, 3]
    # when: meghívja a tesztelendő függvényt
    result = remove_all(numbers, 2)
    # then: ellenőrzi a függvény által visszaadott adatokat
    assert result == [1, 3, 1, 3]


def test_sum():
    numbers = [1, 2, 3, 1, 2, 3]
    result = sum_numbers(numbers)
    assert result == 12


def test_count_positive_numbers():
    numbers = [1, -1, 1, -1, 1, -1]
    result = count_positive_numbers(numbers)
    assert result == 3


def test_is_all_positive():
    numbers = [1, 2, 3, 4, 5]
    result = is_all_positive(numbers)
    assert result == True

def test_is_all_positive_false():
    numbers = [1, 2, 3, -1, 4, 5]
    result = is_all_positive(numbers)
    assert result == False

def test_get_all_positive_numbers():
    numbers = [1, -2, 3, -1, 4, 5]
    result = get_all_positive_numbers(numbers)
    assert result == [1, 3, 4, 5]

def test_double_values():
    numbers = [1, 2, 3]
    result = double_values(numbers)
    assert result == [2, 4, 6]

