#4 задание
number = int(input('enter the number: '))
digit = number%10
number = number//10
while number > 0:
    if number%10 > digit:
        digit = number%10
    number = number//10
print(digit)
