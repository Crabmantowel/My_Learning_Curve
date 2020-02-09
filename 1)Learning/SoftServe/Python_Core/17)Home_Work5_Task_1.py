import math


def distance(x1, y1, x2, y2):
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)


x1, x2, y1, y2 = int(input('Enter x1: ')), int(input('Enter x2: ')), int(input('Enter y1: ')), int(input('Enter y2: '))
print(distance(x1, y1, x2, y2))
