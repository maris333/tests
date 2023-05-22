from unittest.mock import call, Mock

import pytest as pytest

from src.functions import Functions


class TestFunctions:

    @pytest.fixture
    def functions(self):
        return Functions()

    def test_is_prime_should_return_true_for_prime_numbers(self, functions: Functions):
        assert functions.is_prime(2) is True
        assert functions.is_prime(53) is True

    def test_is_prime_should_return_false_for_negative_numbers(self, functions: Functions):
        assert functions.is_prime(-1) is False
        assert functions.is_prime(-53) is False

    def test_is_prime_should_return_false_for_not_prime_numbers(self, functions: Functions):
        assert functions.is_prime(0) is False
        assert functions.is_prime(1) is False
        assert functions.is_prime(51) is False

    def test_fizz_buzz_returns_fizz_with_value_dividable_by_3_and_not_5(self, functions: Functions):
        assert functions.fizz_buzz(3) == "Fizz"
        assert functions.fizz_buzz(9) == "Fizz"

    def test_fizz_buzz_returns_buzz_with_value_dividable_by_5_and_not_3(self, functions: Functions):
        assert functions.fizz_buzz(5) == "Buzz"
        assert functions.fizz_buzz(10) == "Buzz"

    def test_fizz_buzz_returns_fizzbuzz_with_value_dividable_by_3_and_5(self, functions: Functions):
        assert functions.fizz_buzz(15) == "FizzBuzz"
        assert functions.fizz_buzz(30) == "FizzBuzz"

    def test_fizz_buzz_returns_empty_string_with_value_not_dividable_by_3_nor_5(self, functions: Functions):
        assert functions.fizz_buzz(8) == ""
        assert functions.fizz_buzz(17) == ""

    def test_quicksort_returns_sorted_list(self, functions: Functions):
        assert functions.quicksort([-5, 4, 3, 2, 1, 0]) == [-5, 0, 1, 2, 3, 4]

    def test_quicksort_returns_empty_list_for_empty_list(self, functions: Functions):
        assert functions.quicksort([]) == []

    def test_quicksort_returns_sorted_list_for_negative_values(self, functions: Functions):
        assert functions.quicksort([0, -5, -4, -3, -2, -1]) == [-5, -4, -3, -2, -1, 0]

    def test_quicksort_returns_sorted_list_for_same_values(self, functions: Functions):
        assert functions.quicksort([0, 0, 0]) == [0, 0, 0]

    def test_show_message(self, functions):
        mock = Mock(functions.show_message("message"), return_value=None)
        mock(1)
        mock(2)
        calls = [call(1), call(2)]
        mock.assert_has_calls(calls)
