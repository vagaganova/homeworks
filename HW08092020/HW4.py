translater = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}
my_list = []
result = []
try:
    file_obj = open('count', encoding= 'utf-8')
    for line in file_obj:
        tokens = line.replace('\n','').replace(' ','').split('-')
        if tokens[0].lower() in translater:
            result.append(translater[tokens[0].lower()] +' - '+ tokens[1] +'\n')
except IOError:
    print('Произошла ошибка ввода-вывода!')
finally:
    file_obj.close()

try:
    file_input = open('count', 'w', encoding= 'utf-8')
    file_input.writelines(result)
except IOError:
    print('Произошла ошибка ввода-вывода!')
finally:
    file_input.close()