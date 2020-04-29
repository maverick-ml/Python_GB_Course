# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

test_str = 'Cat is a pet ฅʕ•̫͡•ʔฅ'
test_int = 27
test_float = 0.4
test_list = ['text', 456, 37.3, None]
test_tuple = (234, 37.8, 'word', True)
test_set = {400, None, 'night', 37.3}
test_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'e'}

result_list = [test_str, test_int, test_float, test_list, test_tuple, test_set, test_dict]

for el in result_list:
    print(el, '=', type(el))
