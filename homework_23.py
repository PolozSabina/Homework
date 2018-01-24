import random

var = random.randint(0, 10)

while True:
    choice = int(input('Угадай число:'))
    if choice == var:
        print('Вы угадали!')
        break
    elif choice > var:
        print('Меньше')
    else:
        print('Больше!')

