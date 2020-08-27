#2 задание
time = int(input('enter time in seconds: '))
hours = int(time/3600)
minutes = int((time%3600)/60)
seconds = int((time%3600)%60)
print(f'{hours:2d}:{minutes:2d}:{seconds:2d}')
