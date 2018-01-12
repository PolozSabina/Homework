v1 = 12
v2 = 18


def have_trains_crashed(v1, v2):
    train_A = 4
    train_B = 6
    time_train_A = train_A / v1
    time_train_B = train_B / v2
    return time_train_B <= time_train_A

if have_trains_crashed(v1, v2):
    print('Поезда столкнутся')
else:
    print('Поезда нестолкнутся')
