my_str = input('Введи строку: ')
el = my_str.split(' ')
for i, el in enumerate(el, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")