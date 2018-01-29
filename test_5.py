value_1 = float(input('Введи первое число:'))
value_2 = float(input('Введите второе число:'))

number = 10
distance_for_value_1 = abs(number - value_1)
distance_for_value_2 = abs(number - value_2)

if distance_for_value_1 < distance_for_value_2:
    print('Первое значение ближе к %d' % number)
else:
    print('Второе значение ближе к %d' % number)













