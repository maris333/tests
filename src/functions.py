class Functions:
    def is_prime(self, number: int):
        print((number ** 0.5))
        if number < 2:
            return False
        for i in range(2, number - 1):
            if number % i == 0:
                return False
        return True

    def fizz_buzz(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return ""

    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self.quicksort(left) + middle + self.quicksort(right)

    def show_message(self, msg):
        print(f"Your message: {msg}")
