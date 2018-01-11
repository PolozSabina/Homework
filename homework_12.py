#----WITH STR-----

var_1 = '123'

def sum_of_digits(number): # returns int
    number_1 = int(number[:1])
    number_2 = int(number[1:2])
    number_3 = int(number[2:])
    sum = number_1 + number_2 + number_3
    return sum

print(sum_of_digits(var_1))


#---Without STR------

var_2 = 564

def sum_of_digits_2(number):
    number_1 = number // 100
    number_2 = (number - number_1*100) // 10
    number_3 = number-number_1*100-number_2*10
    sum_2 = number_1 + number_2 + number_3
    return sum_2


print(sum_of_digits_2(var_2))
