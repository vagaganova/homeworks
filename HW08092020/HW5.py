from functools import reduce

with open ('summary', 'r+') as f_obj:
    f_obj.write('1 2 3 4 56 34 32 98 56')
    sum_obj = f_obj.readline()
    print(reduce(lambda x,y: x+y, map(lambda str_num: int(str_num), sum_obj.split(' ')),0))
