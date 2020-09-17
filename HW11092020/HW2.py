class Road:
    __length = None
    __width = None
    weigth = None
    thick = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Create roadbed object')

    def intake(self):
        self.weigth = 25
        self.thick = 5
        intake = self.length * self.width * self.weigth * self.thick / 1000
        print(f'Will take {intake} tons for the cover')

roadbed = Road(5000, 20)
roadbed.intake()