import pytest
from pytest_bdd import scenario, given, parsers, when, then

from src.functions import Functions


@scenario('fizz_buzz.feature', 'Number divisible by 3')
def test_number_divisible_by_3():
    pass


@scenario('fizz_buzz.feature', 'Number divisible by 5')
def test_number_divisible_by_5():
    pass


@scenario('fizz_buzz.feature', 'Number divisible by both 3 and 5')
def test_number_divisible_by_both():
    pass


@scenario('fizz_buzz.feature', 'Number not divisible by 3 or 5')
def test_number_not_divisible():
    pass


@pytest.fixture()
def functions():
    return Functions()


@pytest.fixture
@given(parsers.parse('a number is divisible by 3'))
def given_divisible_by_3():
    return 3


@pytest.fixture
@given(parsers.parse('a number is divisible by 5'))
def given_divisible_by_5():
    return 5


@pytest.fixture
@given(parsers.parse('a number is divisible by both 3 and 5'))
def given_divisible_by_both():
    return 15


@pytest.fixture
@given(parsers.parse('a number is not divisible by 3 or 5'))
def given_not_divisible():
    return 7


@when('I perform Fizz Buzz on the number 3')
def when_perform_fizz_buzz_3(given_divisible_by_3, functions):
    return functions.fizz_buzz(given_divisible_by_3)


@then(parsers.parse('it should return "Fizz"'))
def then_check_result_3(given_divisible_by_3, functions):
    assert when_perform_fizz_buzz_3(given_divisible_by_3, functions) == "Fizz"


@when('I perform Fizz Buzz on the number 5')
def when_perform_fizz_buzz_5(given_divisible_by_5, functions):
    return functions.fizz_buzz(given_divisible_by_5)


@then(parsers.parse('it should return "Buzz"'))
def then_check_result_5(given_divisible_by_5, functions):
    assert when_perform_fizz_buzz_5(given_divisible_by_5, functions) == "Buzz"


@when('I perform Fizz Buzz on the number 15')
def when_perform_fizz_buzz_3_and_5(given_divisible_by_both, functions):
    return functions.fizz_buzz(given_divisible_by_both)


@then(parsers.parse('it should return "FizzBuzz"'))
def then_check_result_3_and_5(given_divisible_by_both, functions):
    assert when_perform_fizz_buzz_3_and_5(given_divisible_by_both, functions) == "FizzBuzz"


@when('I perform Fizz Buzz on the number 7')
def when_perform_fizz_buzz_7(given_not_divisible, functions):
    return functions.fizz_buzz(given_not_divisible)


@then(parsers.parse('it should return an empty string'))
def then_check_result_7(given_not_divisible, functions):
    assert when_perform_fizz_buzz_7(given_not_divisible, functions) == ""
