prod_list = []
prod_str = input('введите данные о товаре название, цену, количество, ед.изм через запятую:')
index = 1
while prod_str != 'end':
    temp = prod_str.split()
    prod_list.append((index, dict(name= temp[0], cost = temp[1], number = temp[2], value = temp[3])))
    index +=1
    prod_str = input('введите данные о товаре название, цену, количество, ед.изм через запятую:')
print(prod_list)
result = {'name':set(), 'cost':set(), 'number':set(), 'value':set()}
for i in prod_list:
    result['name'].add(i[1]['name'])
    result['cost'].add(i[1]['cost'])
    result['number'].add(i[1]['number'])
    result['value'].add(i[1]['value'])
print(result)