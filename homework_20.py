#Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел среди 100 случайно сгенерированных чисел в произвольном числовом диапазоне. Т.е. от суммы четных чисел вычесть сумму нечетных чисел.

import random

def diff_even_odd(num_limit, lower_bound, upper_bound):
    random_vars = []
    even = 0
    odd = 0

    for i in range(num_limit):
        random_vars.append(random.randint(lower_bound, upper_bound))

        if random_vars[i] % 2 == 0:
            even += random_vars[i]
        else:
            odd += random_vars[i]

        res = even - odd
        return res

print(diff_even_odd(100, 1, 200))