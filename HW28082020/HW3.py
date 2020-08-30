
month_number = int(input('enter the month from 1 to 12: '))
month_dict = {     1: 'Зима', 2:'Зима',
                   3: 'Весна', 4:'Весна',5:'Весна',
                   6:'Лето',7:'Лето',8:'Лето',
                   9:'Осень',10:'Осень',11:'Осень',
                   12:'Зима'}
print(month_dict.get(month_number,'Вы ошиблись с номером месяца'))

month_lst = ['Зима','Зима','Весна','Весна','Весна','Лето','Лето','Лето','Осень','Осень','Осень','Зима']
if((month_number-1)>=0 and (month_number-1)<=11):
    print(month_lst[month_number-1])
else:
    print('Вы ошиблись с номером месяца')