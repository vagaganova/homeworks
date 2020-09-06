from sys import argv
file_name, output, rate, bonus = argv
def salary(output, rate, bonus):
    return (output * rate) + bonus
print('выработка: ', output)
print('ставка: ', rate)
print('премия: ', bonus)
print('Зарплата: ', salary(int(output),int(rate),int(bonus)))