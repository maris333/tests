Feature: Fizz Buzz

  Scenario: Number divisible by 3
    Given a number is divisible by 3
    When I perform Fizz Buzz on the number 3
    Then it should return "Fizz"

  Scenario: Number divisible by 5
    Given a number is divisible by 5
    When I perform Fizz Buzz on the number 5
    Then it should return "Buzz"

  Scenario: Number divisible by both 3 and 5
    Given a number is divisible by both 3 and 5
    When I perform Fizz Buzz on the number 15
    Then it should return "FizzBuzz"

  Scenario: Number not divisible by 3 or 5
    Given a number is not divisible by 3 or 5
    When I perform Fizz Buzz on the number 7
    Then it should return an empty string
