import random

def diff_even_odd(num_limit, lower_bound, upper_bound):
    random_var = []
    even = 0
    odd = 0

    for i in range(num_limit):
        random_var = random.randint(lower_bound, upper_bound)

        if random_var % 2 == 0:
            even += random_var
        else:
            odd += random_var

        res = even - odd
        return res

print(diff_even_odd(100, 1, 200))