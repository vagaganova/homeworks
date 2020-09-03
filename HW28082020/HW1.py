my_int = 2
my_float = 2.2
my_str = ' This is string '
my_list = ['list', 'and one more list']
my_tuple = ('tuple', '3', 'list is not')
my_dict = {'name': 'Valeriya', 'surname': 'Gaganova' , 'age': '24'}

main_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in main_list:
    print(f'{i} is {type(i)}')