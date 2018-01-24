#Написать функцию возвращающую наибольшую цифру случайно сгенерированного 12 ти-значного натурального числа.
import random

n = 123456789123

def get_max_digit(number):
    n = str(number)
    rand_lst = [0]*len(n)

    for i in range(len(n)):
        rand_lst[i] = n[i:i+1]

    max_value = int(max(rand_lst))

    return max_value


print(get_max_digit(n))