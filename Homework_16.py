v1 = 13
v2 = 18

def have_trains_crashed(v1, v2):
    distance_train__a = 4
    distance_train__b = 6
    time_train__a = distance_train__a / v1
    time_train__b = distance_train__b / v2
    return time_train__b <= time_train__a

if have_trains_crashed(v1, v2):
    print('Поезда столкнутся')
else:
    print('Поезда нестолкнутся')
