
class NotANumberError(Exception):
    def __init__(self):
        self.txt = 'Вы пытаетесь добавить в список строку или нецелое число'
    def __str__(self):
        return self.txt


my_list = []
while True:
    try:
        command = input("введите число: ")
        if command == '!s': break
        if not command.isdigit(): raise NotANumberError
    except NotANumberError as err:
        print(err)
    else:
        my_list.append(int(command))
print(my_list)