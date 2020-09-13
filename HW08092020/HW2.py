with open('my_file.txt') as my_file:
    lines = my_file.readlines()
    print ('Количество строк: ', len(lines))
    for i in range(len(lines)):
        if len(lines[i].replace(' ', '').replace('\n','')) > 0:
            print('В строке ', i, ':', len(lines[i].split(' ')))
        else:
            print('В строке ', i, ':','0')
