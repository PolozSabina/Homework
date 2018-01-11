import math

input_a = input('Enter base triangle')
input_b = input('Enter height of triangle')

def triangle_square_and_perimeter(a, b):
    square = int (1/2 * int(a)*int(b))
    hypotenuse = math.sqrt(int(a)**2 + int(b)**2)
    perimetr = int(a) + int(b) + int(hypotenuse)
    return square, perimetr

print(triangle_square_and_perimeter(input_a, input_b))

