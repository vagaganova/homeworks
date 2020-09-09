my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123]
new_list =[my_list[i+1] for i in range(len(my_list)-1) if my_list[i+1]>my_list[i]]
print (list(new_list))


# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123]
# new_list =[i*5 for i in my_list if i%3 == 0]
# print (list(new_list))
