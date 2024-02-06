import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

degrees = float(input("Enter degrees: "))
radians = degrees_to_radians(degrees)
print(f"Output radians: {radians:.2f} ")

#2
def tr(height, base1, base2):
    area = 0.5 * (base1 + base2) * height
    return area

height = float(input("trapezoid: "))
base1 = float(input("first base: "))
base2 = float(input("second base: "))

area = tr(height, base1, base2)
print("The area of the trapezoid is:", area)

#3
import math

def polygon(n, s):
    return (1 / 4) * n * s**2 * (1 / math.tan(math.pi / n))

n = int(input("Enter the number of sides: "))
s = float(input("Enter the length of each side: "))

area = polygon(n, s)
print("The area of the regular polygon is:", area)

#4
def para(base, height):
    return base * height

base = float(input("length of the base: "))
height = float(input("height of the parallelogram: "))

area = para(base, height)
print("The area of the parallelogram is:", area)
