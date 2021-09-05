# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

x1 = input('введите x1: ')
y1 = input('введите y1: ')
x2 = input('введите x2: ')
y2 = input('введите y2: ')


def coeff(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return k, b


coord_list = [x1, y1, x2, y2]

for i in coord_list:
    if i.isdigit():
        pass
    elif i[0] == '-' and i[1:].isdigit():
        pass
    else:
        print('некорректные координаты')
        exit()

k, b = coeff(int(x1), int(y1), int(x2), int(y2))

print(f'y = {k}x + {b}')