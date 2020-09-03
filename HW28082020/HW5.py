my_list = [7,5,3,3,2]
number = input('enter the number: ')
while number != 'exit':
    _number = int(number)
    index = 0
    for i in my_list:
        if i < _number:
            break
        index += 1
    my_list.insert(index,_number)
    print(my_list)
    number = input('enter the number: ')
print(my_list)