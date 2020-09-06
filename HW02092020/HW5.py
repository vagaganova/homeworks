import sys

result = 0
while True:
    line = input('Enter number or special token q for exit: ')
    tokens = line.split(' ')
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'q':
                print(f'Your sum {result}. Program is terminated')
                exit(0)
            else:
                print(f'Your sum {result}. Input error', file=sys.stderr)
                exit(1)