number_1 = float(input('enter the 1st number: '))
number_2 = float(input('enter the 2nd number: '))
def divide(numerator: float, divider: float) -> float:
    if divider == 0:
        print('You try zero division!!!')
        raise ZeroDivisionError
    else:
        return numerator/divider
print (divide(number_1,number_2))