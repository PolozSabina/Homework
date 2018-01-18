import random

def diff_min_max(num_limit, lower_bound, upper_bound):
    rand_lst = [0]*num_limit
    for i in range(len(rand_lst)):
        rand_lst[i] = random.randint(lower_bound, upper_bound)
    max_value = max(rand_lst)
    min_value = min(rand_lst)
    res_diff = max_value - min_value
    return res_diff

print(diff_min_max(10, 4, 100))
