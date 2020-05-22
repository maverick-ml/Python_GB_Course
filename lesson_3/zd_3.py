# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(var_1, var_2, var_3):
    if var_1 >= var_3 and var_2 >= var_3:
        return var_1 + var_2
    elif var_2 < var_1 < var_3:
        return var_1 + var_3
    else:
        return var_2 + var_3


print(f'Результат: {my_func(int(input("Первое число: ")), int(input("Второе число: ")),int(input("Третье число: ")))}')
