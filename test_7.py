# = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def fibonacci(n):
    if n == 1 or n == 2:
        return  1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib_numbers = 10

lst = (sum([fibonacci(i) for i in range(1, fib_numbers+1)]))
print(lst)





