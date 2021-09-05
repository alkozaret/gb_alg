'''
Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
'''

print(5 & 6) # результат 4, так как and выставляет 1, если в обоих операндах в одном разряде стоит 1, 101 и 110 = 100
print(5 | 6) # результат 7, так как or выставляет 0, если в обоих операндах в одном разряде стоит 0, 101 или 110 = 111
print(6 ^ 5) # результат 3, так как xor выставляет 0, если значения разрядов операндов совпадают, 101 xor 110 = 011
print(5 << 2) # результат 20, так как при сдвиге бит влево получается 10100, это 1 * 2^4 + 1 * 2^2 = 20
print(5 >> 2) # результат 1, так как при сдвиге бит влево третий разряд переходит на место первого, 2й и 1й вылетают