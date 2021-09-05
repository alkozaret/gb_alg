'''
По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
равнобедренным или равносторонним.
'''

ab = input('введите длину первой стороны треугольника: ')
bc = input('введите длину второй стороны треугольника: ')
ac = input('введите длину третьей стороны треугольника: ')


def isosceles(a, b, c):
    if a == b and c < a or a == b and c < a + b:
        return True


def scalene(a, b, c):
    if a < b > c and b < a + c:
        return True


if ab.isdigit() and ac.isdigit() and bc.isdigit():
    ab = int(ab)
    bc = int(bc)
    ac = int(ac)
    if ab == bc == ac:
        print('треугольник равносторонний')
    elif isosceles(ab, bc, ac) or isosceles(ac, ab, bc) or isosceles(ac, bc, ab):
        print('треугольник равносторонний')
    elif scalene(ab, bc, ac) or scalene(bc, ab, ac) or scalene(ab, ac, bc):
        print('треугольник разносторонний')
    else:
        print('треугольника не существует')
else:
    print('некорректный ввод данных')
    exit()