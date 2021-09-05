'''
Написать программу, которая генерирует в указанных пользователем границах:

    случайное целое число;
    случайное вещественное число;
    случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
'''

import random

z = input('введите два целых числа через проблел: ')
r = input('введите два числа через проблел: ')
l = input('введите две латинских буквы через проблел: ').lower()


def check(string):
    simbol = string.split()
    if len(string) > 2 and ' ' in string:
        if string.replace('-', '').replace(' ', '').isdigit() and int(simbol[0]) <= int(simbol[1]):
            pass
        elif string.replace('-', '').replace(' ', '').isalpha() and int(ord(simbol[0])) <= int(ord(simbol[1])):
            pass
        else:
            print('некорректный ввод данных')
            exit()
        return string
    else:
        print('некорректный ввод данных')
        exit()


z_list = check(z).split()
r_list = check(r).split()
l_list = check(l).split()

print(random.randint(int(z_list[0]), int(z_list[1])))
print(random.uniform(float(r_list[0]), float(r_list[1])))
print(chr(random.randint(ord(l_list[0]), ord(l_list[1]))))