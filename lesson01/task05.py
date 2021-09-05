# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

l = input('введите две латинских буквы через проблел: ').lower()


def check(string):
    simbol = string.split()
    if len(string) > 2 and ' ' in string:
        if string.replace('-', '').replace(' ', '').isalpha() and int(ord(simbol[0])) <= int(ord(simbol[1])):
            pass
        else:
            print('некорректный ввод данных')
            exit()
        return string
    else:
        print('некорректный ввод данных')
        exit()


l1 = check(l).split()[0]
l2 = check(l).split()[1]

print(f'буква {l1} {ord(l1)-96}-я в алфавите\n'
      f'буква {l2} {ord(l2)-96}-я в алфавите\n'
      f'количество букв между ними равно {ord(l2) - ord(l1) - 1}')