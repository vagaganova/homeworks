import re
from functools import reduce

with open('practice', encoding='utf-8') as pract_obj:
 lines = pract_obj.readlines()
 new_dict = {}
 for i in lines:
    list_str = i.split(':')
    number = re.findall(r'\d+', i)
    new_dict[list_str[0]] = reduce(lambda x,y: x+y, map(lambda str_num: int(str_num), number),0)
print(new_dict)