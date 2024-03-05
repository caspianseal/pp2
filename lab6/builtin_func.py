#1
import math

def multiply_numbers(nums):
    return math.prod(nums)

numbers = [2, 3, 4, 5]
result = multiply_numbers(numbers)
print("Result:", result)

#2
def count_case_letters(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

input_string = "Hello World"
upper, lower = count_case_letters(input_string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)

#3
def is_p(string):
    return string == string[::-1]

input_string = "radar"
if is_p(input_string):
    print("Palindrome")
else:
    print("Not Palindrome")

#4
import time
import math

def sqrtmilli(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

number = 25100
milliseconds = 2123
res = sqrtmilli(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {res}")

#5
def all_true(tuple_of_bools):
    return all(tuple_of_bools)

tuple_values = (True, True, False, True)
print(all_true(tuple_values))