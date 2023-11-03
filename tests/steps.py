from pytest_bdd import given, parsers, when, then

from src.functions import Functions


@given(parsers.parse('a number is divisible by {divisor:d}'))
def given_divisible_by(functions, divisor):
    number = 9 if divisor == 3 else 10 if divisor == 5 else 15
    return number

@when('I perform Fizz Buzz on the number')
def when_perform_fizz_buzz(given):
    your_class_instance = Functions()
    return your_class_instance.fizz_buzz(given)

@then(parsers.parse('it should return "{expected_result}"'))
def then_check_result(when_perform_fizz_buzz, expected_result):
    assert when_perform_fizz_buzz == expected_result
