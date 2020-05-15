# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen().
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.


from itertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        yield factorial(el)


gen = fibo_gen()
num = 0
for n in gen:
    if num < 15:
        print(n)
        num = num + 1
    else:
        break
