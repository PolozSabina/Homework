import random

def diff_even_odd(num_limit, lower_bound, upper_bound):
    random_vars = []
    even = 0
    odd = 0

    for i in range(num_limit):
        random_vars = random.randint(lower_bound, upper_bound)

        if random_vars % 2 == 0:
            even += random_vars
        else:
            odd += random_vars

        res = even - odd
        return res

print(diff_even_odd(100, 1, 200))