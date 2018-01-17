import math

x1 = 4
y1 = 7
r1 = 2

x2 = 2
y2 = 2
r2 = 5

def cirles_intersects(x1, y1, r1, x2, y2, r2):
    dist = math.sqrt((x2 - x1)**2 +(y2 - y1)**2)
    sum__r = r1 + r2
    return dist <= sum__r and dist >= abs(r1-r2)

if cirles_intersects(x1, y1, r1, x2, y2, r2):
    print('Oкружности пересекаются')
else:
    print('Окружности не пересекаются')

