class Car():
    name = None
    speed = None
    color = None
    is_police = False
    def __init__(self, name, speed, color, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return 'car is moving\n'
    def stop(self):
        return 'stop'
    def turn(self, direction):
        return 'the car turn to the ' + direction
    def show_speed(self):
        return self.speed

class TownCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, is_police= False)
    def show_speed(self):
        if self.speed > 60:
            print('speed limit is exceeded')
        return self.speed

class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, is_police= False)

class WorkCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, is_police=False)
    def show_speed(self):
        if self.speed > 40:
            print('speed limit is exceeded')
        return self.speed

class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


kia_rio = TownCar('kia', 80, 'red')
kia_rio.go()
kia_rio.show_speed()
kia_rio.turn(direction='left')
kia_rio.stop()
print(kia_rio.name, kia_rio.speed,kia_rio.color)
print(kia_rio.go(), kia_rio.turn('left'), kia_rio.stop(), '\n')

audi_r8 = SportCar('audi', 80, 'black')
audi_r8.go()
audi_r8.show_speed()
audi_r8.turn(direction= 'right')
audi_r8.stop()
print(audi_r8.name, audi_r8.speed, audi_r8.color)
print(audi_r8.go(), audi_r8.turn('left'), audi_r8.stop(), '\n')

chevrolet_lanos = WorkCar('chevrolet', 50, 'blue')
chevrolet_lanos.go()
chevrolet_lanos.show_speed()
chevrolet_lanos.turn(direction= 'right')
chevrolet_lanos.stop()
print(chevrolet_lanos.name, chevrolet_lanos.speed, chevrolet_lanos.color)
print(chevrolet_lanos.go(), chevrolet_lanos.turn('left'), chevrolet_lanos.stop(), '\n')

ford_focus = PoliceCar('ford', 60, 'gray')
ford_focus.go()
ford_focus.show_speed()
ford_focus.turn(direction= 'left')
ford_focus.stop()
print(ford_focus.name, ford_focus.speed, ford_focus.color)
print(ford_focus.go(), ford_focus.turn('left'), ford_focus.stop())