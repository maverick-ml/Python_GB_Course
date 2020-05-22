# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


my_f = open('text2.txt', 'r', encoding='utf-8')
text = my_f.readlines()
lines = 0

print(f'Количество строк: {len(text)}')

for el in text:
    lines += 1
    n = el.split()
    print(f'В строке №{lines} - {str(len(n))} слов')

my_f.close()
