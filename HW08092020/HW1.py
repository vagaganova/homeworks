with open('my_file.txt', 'a') as my_file:
    is_zero = input('Введите строки в файл:')
    while len(is_zero.replace(' ', '')) > 0:
     my_file.writelines([is_zero, '\n'])
     is_zero = input('Введите строки в файл:')
print('Файл закрыт')