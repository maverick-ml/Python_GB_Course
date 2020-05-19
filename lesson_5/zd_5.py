# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


my_f = open('text5.txt', 'w', encoding='utf-8')
text = input('Введите числа через пробел: ')
my_f.writelines(text)
my_f.close()

my_c = open('text5.txt', 'r', encoding='utf-8')
my_lst = my_c.read().split()
print(f'Сумма чисел: {(sum(map(int, my_lst)))}')
my_c.close()
