# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = input('enter a number: ')


def oper(num):
    summ = 0
    mult = 1
    for i in range(len(num)):
        summ = summ + int(num[i])
        mult = mult * int(num[i])
    return summ, mult


if num.isdigit():
    summ, mult = oper(num)
elif num[0] == '-' and num[1:].isdigit():
    num = num[1:]
    summ = f'-{oper(num)[0]}'
    mult = f'-{oper(num)[1]}'
else:
    print('error')
    exit()

print(summ)
print(mult)