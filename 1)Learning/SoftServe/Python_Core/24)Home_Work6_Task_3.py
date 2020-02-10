# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5
# below the number passed in.
# Note: If the number is a multiple of both 3 and 5, only count it once.
import random


def randomizer_to_20():
    return random.randrange(10, 20)


def solution(number):
    all_needed_numbers = 0
    for listed_numbers in range(number):
        if (listed_numbers % 3 == 0) or (listed_numbers % 5 == 0):
            all_needed_numbers += listed_numbers
    return all_needed_numbers


some_number = randomizer_to_20()
print(solution(some_number))
