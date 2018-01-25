import random

def get_max_digit(number):
    n_lst = str(number)
    rand_lst = [i for i in n_lst]
    max_value = int(max(rand_lst))
    return max_value

n = random.randint(100000000000, 999999999999)
print(n)

print(get_max_digit(n))

