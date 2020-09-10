import json
profit = {}
loss = {}
with open ('firms', encoding='utf-8') as my_firm:
    my_list = my_firm.readlines()
    count = 0
    cost = 0
    for i in my_list:
        list_str = i.replace('\n','').split(' ')
        temp_profit = int(list_str[2]) - int(list_str[3])
        if temp_profit > 0:
            profit[list_str[0]] = temp_profit
            count +=1
            cost += temp_profit
        else:
            loss[list_str[0]] = temp_profit
    average_profit = 0
    if count > 0:
        average_profit = cost/count
    avr = dict(average_profit= average_profit)
    result=[profit,loss,avr]
with open('my_file.json', 'w') as write_f:
        json.dump(result, write_f)


