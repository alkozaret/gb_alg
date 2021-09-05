# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

a = input('введите первое число: ')
b = input('введите второе число: ')
c = input('введите третье число: ')


def check(sign):
    if sign[0] == '-':
        if sign[1:].isdigit():
            return int(sign)
        else:
            print('некорректный ввод данных')
            exit()
    else:
        if sign.isdigit():
            return int(sign)
        else:
            print('некорректный ввод данных')
            exit()


num_list = []
for i in [a, b, c]:
    num_list.append(check(i))

num_list.remove(max(num_list))
num_list.remove(min(num_list))

print(f'средное число {num_list[0]}')
