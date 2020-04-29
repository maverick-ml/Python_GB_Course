# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = str(input('Введите число: '))
summer = int(num) + int(num + num) + int(num + num + num)
print('Считаем:', num, '+', num + num, '+', num + num + num, '=', summer)
