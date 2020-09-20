class Cell:
    def __init__(self,slotcount):
        self.slotcount = slotcount

    def __add__(self, other):
        if(not isinstance(other,Cell)):
            print("Не складывается с неклеткой")
            raise ArithmeticError
        return Cell(self.slotcount + other.slotcount)

    def __sub__(self, other):
        if (not isinstance(other, Cell)):
            print("Не производятся операции с неклеткой")
            raise ArithmeticError
        if(self.slotcount < other.slotcount):
            print("Клетка имеет больше ячеек")
            raise ArithmeticError
        return Cell(self.slotcount - other.slotcount)

    def __mul__(self, other):
        if (not isinstance(other, Cell)):
            print("Не производятся операции с неклеткой")
            raise ArithmeticError
        return Cell(self.slotcount * other.slotcount)

    def __truediv__(self, other):
        if(not isinstance(other,Cell)):
            print("Не производятся операции с неклеткой")
            raise ArithmeticError
        if (other.slotcount == 0 ):
            print("Клетка не имеет ячеек")
            raise ZeroDivisionError
        return Cell(self.slotcount // other.slotcount)

    def make_order(self, columns):
        __n = self.slotcount // columns
        __countappendix = self.slotcount % columns
        __row = '*'*columns + '\n'
        __appendix = '*'*__countappendix
        if(__countappendix>0): return __row*__n + __appendix
        return (__row*__n + __appendix)[0:-1]

cell1 = Cell(15)
cell2 = Cell(5)
print((cell1 + cell2).make_order(7) + '\n')
print((cell1 - cell2).make_order(3)+ '\n')
print((cell1 / cell2).make_order(5)+ '\n')
print((cell1 * cell2).make_order(25))