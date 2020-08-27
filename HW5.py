#5 задание
gain = float(input('Введите выручку: ')) #выручка
cost = float(input('Введите издержки: ')) #издержки
money = gain - cost
if money > 0:
    print('Поздравляю, мы не в нуле!У нас прибыль:',int(money))
    print('Рентабельность равна: ',(money/gain))
    people = int(input('Сколько сотрудников в фирме? '))
    print('Прибыль на каждого сотрудника:', int(money/people))
else:
    print('no money - no honey')
