my_list = list(input('enter the values:'))

i = 0
while i <= (len(my_list)-1-(len(my_list) % 2 )):
    element = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i+1] = element
    i += 2
print(my_list)