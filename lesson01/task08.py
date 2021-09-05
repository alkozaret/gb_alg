# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = input('введите год: ')

if year.isdigit():
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('високосный')
    else:
        print('не високосный')
else:
    print('некорректный ввод данных')
    exit()
