from functools import reduce

with open('salary.txt') as my_salary:
    workers = list(map(lambda x: dict(name=x.split(' ')[0],salary=float(x.split(' ')[1])), my_salary.readlines()))
    low_workers =list(map(lambda x:x['name'],filter(lambda x:x['salary']<20000,workers)))
    average = reduce(lambda x,y:x + y,map(lambda x:x['salary'],workers),0.0)/len(workers)
    print(low_workers)
    print(average)