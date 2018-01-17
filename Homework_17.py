import math

a = 1
b = 2
c = 1

def solve_quadratic_equation(a, b, c):
    discriminant = b**2-4*a*c
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        x = -b / (2 * a)
        return x, None
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2

def print_nice(symbol = 'SP'):
    print(symbol*20)

print(solve_quadratic_equation(a,b,c))
