import math

input_a = int(input('Enter base triangle'))
input_b = int(input('Enter height of triangle'))

def triangle_square_and_perimeter(a, b):
    square = 1/2 * a*b
    hypotenuse = math.sqrt(a**2 + b**2)
    perimetr = a + b + hypotenuse
    return square, perimetr

print(triangle_square_and_perimeter(input_a, input_b))

