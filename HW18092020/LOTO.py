import random
class Card:

    def __init__(self, name):
        self._name = name
        self._number_of_values = 15
        self._matrix = []
        __barrels = list(range(1,91))
        random.shuffle(__barrels)
        __barrels= [(__barrels[0:5]),(__barrels[5:10]),(__barrels[10:15])]

        for row in range(0, 3):
            __randomcols = list(range(0,9))
            random.shuffle(__randomcols)
            __randomcols = __randomcols[:6]
            __randomcols.sort()
            __line = [None for column in range(0, 9)]
            __barrels[row].sort()
            while len(__barrels[row]):
                __line[__randomcols.pop()] = __barrels[row].pop()
            self._matrix.append(__line)
    def _clear(self):
        for row in range(0, 3):
            for column in range(0, 9):
                self._matrix[row][column] = None
    @property
    def is_empty(self):
        return not self._number_of_values

    def output(self):
        title = ' ' + self._name + ' '
        if len(title) <= 24:
            print(title.center(26, '-'))
        else:
            print('-'*26)
        for y in self._matrix:
            string = ''
            for x in y:
                if not x:
                    string += '   '
                elif x == -1:
                    string += ' - '
                else:
                    string += '{:>2} '.format(str(x))
            print(string)
        print('-'*26)

    def find(self, value):
        for row in self._matrix:
            if row.count(value):
                return True
        return False

    def cross_out(self, value):
        for row in range(0, 3):
            for column in range(0, 9):
                if self._matrix[row][column] == value:
                    self._matrix[row][column] = -1
                    self._number_of_values -= 1
                    return value
        return None


def pouch_of_barrels():
    __barrels = list(range(1, 91))
    random.shuffle(__barrels)
    for barrel in __barrels:
        yield barrel



last_comp_move = True
mistake_chance = 0.5

player_card = Card('Ваша карточка')
comp_card = Card('Карточка компьютера')

print('Игра начинается'.upper())

player_loss = False
draw_flag = False

game_pouch = pouch_of_barrels()
for new_barrel in game_pouch:
    print('\nНовый бочонок: {}'.format(new_barrel))
    player_card.output()
    comp_card.output()

    if input('Зачеркнуть цифру? (y/n) ') == 'y':
        if player_card.cross_out(new_barrel):
            print('Число {} вычеркнуто из вашей карточки.'.format(new_barrel))
            if player_card.is_empty and not last_comp_move:
                break
        else:
            print('Будьте внимательнее! Числа {} нет в вашей карточке.'.format(new_barrel))
            player_loss = True
            if not last_comp_move:
                break
    else:
        if player_card.find(new_barrel):
            print('Будьте внимательнее! В вашей карточке есть число {}.'.format(new_barrel))
            player_loss = True
            if not last_comp_move:
                break

    if mistake_chance and random.uniform(0, 99) < mistake_chance:
        print('Компьютер ошибается! В его карточке {} {}'.format(
              'есть число' if comp_card.find(new_barrel) else 'нет числа', new_barrel))
        if player_loss:
            draw_flag = True
        break
    else:
        if comp_card.cross_out(new_barrel):
            print('Компьютер вычёркивает число {} из своей карточки.'.format(new_barrel))

    if player_card.is_empty and comp_card.is_empty:
        draw_flag = True
        break
    if player_card.is_empty:
        break
    if comp_card.is_empty:
        player_loss = True
        break
    if player_loss:
        break

if draw_flag:
    print('Игра окончена. Ничья!')
elif player_loss:
    print('Игра окончена. Вы проиграли!')
else:
    print('Игра окончена. Вы выиграли!')