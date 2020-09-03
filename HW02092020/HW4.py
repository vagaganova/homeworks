#1 способ
def my_func(x: float, y: int):
    return x ** y
print (my_func(2, 3))


#2 способ
def my_func(x: float, y: int):
    result = 1
    step = 1
    while step <= abs(y):
        result *= x
        step += 1
    if y > 0:
        return result
    else:
        return 1/result
print (my_func(2, 1))


#3 способ
def my_func(x: float, y: int):
    result = 1
    for i in range (abs(y)):
        result *= x
    if y > 0:
        return result
    else:
        return 1/result
# print (my_func(2, 0))


#4 способ
from functools import reduce

def my_func(x: float, y: int):
    if y==0:return 1
    result = reduce(lambda a,b:a*b,map(lambda _x:x,range(abs(y))))
    if y > 0:
        return result
    else:
        return 1/result
print (my_func(2, 0))
