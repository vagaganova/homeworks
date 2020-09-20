class myZeroDivizionError(Exception):
    def __init__(self):
        self.txt = 'Вы пытаетесь поделить на ноль'
    def __str__(self):
        return self.txt

try:
    numerator = int(input('введите числитель'))
    divider = int(input('введите знаменатель'))
    if divider == 0: raise myZeroDivizionError
    d = numerator/divider
except myZeroDivizionError as err:
    print(err)
else:
    print(d)