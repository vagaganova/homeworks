from abc import abstractmethod, ABC


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):

    def __init__(self,name,size):
        self.__name = name
        self.__size = size

    def __str__(self):
        return "На пальто " \
               + self.__name \
               + " потратится "\
               + str(self.consumption)
    @property
    def consumption(self):
        return (self.__size/6.5 + 0.5)

class Suit(Clothes):

    def __init__(self,name,height):
        self.__name = name
        self.__height = height

    def __str__(self):
        return "На костюм " \
               + self.__name \
               + " потратится "\
               + str(self.consumption)
    @property
    def consumption(self):
        return (self.__height*2 + 0.3)

mycoat = Coat("Мое пальто",12.5)
print(mycoat)
print(mycoat.consumption)
mySuit = Suit("Мой костюм",12.5)
print(mycoat)
print(mycoat.consumption)