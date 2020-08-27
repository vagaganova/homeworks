#6 задание
first_day_km = float(input('Результат в километрах в первый день: '))
last_day_km = float(input('Результат в километрах в другой день: '))
day = 1
while last_day_km > first_day_km:
    day = day + 1
    first_day_km = first_day_km * 1.1
print(day)
