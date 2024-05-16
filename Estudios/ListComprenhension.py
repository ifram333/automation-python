fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# 1. 

number_plus_one = [number + 1 for number in numbers]

# 2.

uppercased_fruits = [fruit.upper() for fruit in fruits]

# 3.

capitalized_fruits = [fruit.capitalize() for fruit in fruits ]

# 4.

import re
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if len(re.sub(r"[^aeiouAEIOU]", "", fruit)) > 2]

# 5. 

fruits_with_only_two_vowels = [fruit for fruit in fruits if len(re.sub(r"[^aeiouAEIOU]", "", fruit)) == 2]

# 6.

fruits_with_more_than_five_letters = [fruit for fruit in fruits if len(fruit) > 5]

# 7.

number_characters_fruit = [len(fruit) for fruit in fruits]

# 8.

fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]

# 9. 

even_numbers = [number for number in numbers if (number % 2 == 0) and (number > 0)]

# 10.

def is_prime(number: int) -> bool:
    if number < 0:
        number *= -1
    
    if number == 1:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

primes = [number for number in numbers if is_prime(number)]

if __name__ == "__main__":
    print(primes)