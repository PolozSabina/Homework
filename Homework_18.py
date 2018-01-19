
def sum_symbol_codes(first, last):
    var_1 = ord(first)
    var_2 = ord(last)
    result = 0
    for i in range(var_2 - var_1 + 1):
        result = result + var_1 + i
    return result

print(sum_symbol_codes('a', 'c'))


