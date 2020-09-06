def my_func(*args):
    list = sorted(args, reverse=True)
    return list[0] + list[1]
print (my_func(9,96,-1))

#2 способ
def my_func(num_1: float, num_2: float, num_3: float)-> float:
    list = sorted([num_1,num_2,num_3], reverse=True)
    return list[0] + list[1]
print (my_func(-9,96,-1))