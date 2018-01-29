number = input('Enter your number:')
number = int(number)

odd = 1
while number > 0:
    if not number % 2 == 0:
        number_str = str(number)
        odd *= int(number_str[-1])
    number = number // 10
print("multyply odd: %d" % (odd))

