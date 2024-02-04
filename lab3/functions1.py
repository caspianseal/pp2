#example 1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

#example 2
def fahrenheit_to_centigrade(fahrenheit):
    centigrade = (5 / 9) * (fahrenheit - 32)
    return centigrade

#example 3
def solve(numheads, numlegs):
    # Calculate the number of rabbits
    rabbits = (numlegs - 2 * numheads) / 2
    # Calculate the number of chickens
    chickens = numheads - rabbits
    # Check if the number of rabbits and chickens are both non-negative integers
    if rabbits >= 0 and chickens >= 0 and rabbits == int(rabbits) and chickens == int(chickens):
        return int(chickens), int(rabbits)

#example 4
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    """Filter prime numbers from a list."""
    return [num for num in numbers if is_prime(num)]

#example 5
from itertools import permutations

def print_permutations(string):
    """Print all permutations of a string."""
    # Generate all permutations
    perms = permutations(string)
    # Print each permutation
    for perm in perms:
        print(''.join(perm))

#example 6
def reverse_sentence(sentence):
    """Return a sentence with the words reversed."""
    # Split the sentence into words
    words = sentence.split()
    # Reverse the order of words
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

#example 7
def has_33(nums):
    """Check if the list contains a 3 next to a 3 somewhere."""
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#example 8
def spy_game(nums):
    """Check if the list contains 007 in order."""
    # Initialize variables to track the indices of 0, 0, and 7
    index_0 = index_0_2 = index_7 = None

    # Iterate through the list to find the indices of 0, 0, and 7
    for i, num in enumerate(nums):
        if num == 0:
            if index_0 is None:
                index_0 = i
            elif index_0_2 is None:
                index_0_2 = i
        elif num == 7:
            index_7 = i

    # Check if all indices are found and in the correct order
    if index_0 is not None and index_0_2 is not None and index_7 is not None:
        if index_0 < index_0_2 < index_7:
            return True
    return False

#example 9
import math

def sphere_volume(radius):
    """Compute the volume of a sphere given its radius."""
    volume = (4/3) * math.pi * radius ** 3
    return volume

#example 10
def unique_elements(input_list):
    """Return a new list with unique elements."""
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#example 11
def is_palindrome(word):
    """Check whether a word or phrase is a palindrome."""
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()
    # Check if the word is equal to its reverse
    return word == word[::-1]

#example 12
def histogram(nums):
    """Print a histogram of the frequencies of integers in the list."""
    for num in nums:
        print('*' * num)

#example 13
import random

def guess_the_number():
    """Play the 'Guess the number' game."""
    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    num_guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break

# Call the function to play the game
guess_the_number()