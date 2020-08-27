#1 задание
street = 'Leningradskiy prospect'
house_number = 39.79
that_street = input('enter street name:')
if that_street == street:
    print('ok, and how about house number?')
    that_house_number = float(input('enter house number:'))
    if that_house_number == house_number:
        print('welcome to mail.ru group')


#2 задание
time = int(input('enter time in seconds: '))
hours = int(time/3600)
minutes = int((time%3600)/60)
seconds = int((time%3600)%60)
print(f'{hours:2d}:{minutes:2d}:{seconds:2d}')

#3 задание
number = input('enter the number: ')
print (int(number) + int(number*2) + int(number*3))


#4 задание
number = int(input('enter the number: '))
digit = number%10
number = number//10
while number > 0:
    if number%10 > digit:
        digit = number%10
    number = number//10
print(digit)

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

#6 задание
first_day_km = float(input('Результат в километрах в первый день: '))
last_day_km = float(input('Результат в километрах в другой день: '))
day = 1
while last_day_km > first_day_km:
    day = day + 1
    first_day_km = first_day_km * 1.1
print(day)
