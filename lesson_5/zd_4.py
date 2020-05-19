# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_f = open('text4a.txt', 'r', encoding='utf-8')
new_f = open('text4b.txt', 'w', encoding='utf-8')
translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
lst = []

for el in my_f:
    el = el.split(' ', 1)
    lst.append(translate[el[0]] + ' ' + el[1])
new_f.writelines(lst)

my_f.close()
new_f.close()
