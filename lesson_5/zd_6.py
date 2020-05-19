# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.


import os

# Приводим данные к удобному виду

my_f = open('text6.txt', 'r', encoding='utf-8')
new_f = open('text6b.txt', 'w', encoding='utf-8')

for el in my_f:
    new_f.write(el.replace('(л)', '').replace('(лаб)', '').replace('(пр)', '').replace('.', '').replace('—', '0'))

my_f.close()
new_f.close()

# Формируем словарь

new_f = open('text6b.txt', 'r', encoding='utf-8')

dic = {}

for el in new_f:
    faculty, lecture, practice, lab = el.split()
    dic[faculty] = int(lecture) + int(practice) + int(lab)

print(f'Общее количество часов по предметам: {dic}')

new_f.close()

os.remove('text6b.txt')  # Удаляем, т.к. по заданию он не нужен
