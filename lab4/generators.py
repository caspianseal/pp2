def gen_sq(N):
    for i in range(N):
        yield i ** 2
N = 5
squares_generator = gen_sq(N)
for square in squares_generator:
    print(square)

#2
def gen(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def main():
    n = int(input("Enter a number (n): "))
    even_numbers = gen(n)
    print("Even numbers between 0 and", n, "are:", end=" ")
    print(*even_numbers, sep=", ")

if __name__ == "__main__":
    main()

#3
def div34(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
def main():
    n = int(input("Enter a number (n): "))
    divisible_gen = div34(n)
    print("Numbers divisible by both 3 and 4 between 0 and", n, "are:")
    for num in divisible_gen:
        print(num)

#4
def sq(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Test the generator with a for loop
a = 3
b = 7
print(f"Squares of numbers from {a} to {b}:")
for square in sq(a, b):
    print(square)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = 5
print(f"Counting down from {n} to 0:")
for num in countdown(n):
    print(num)
