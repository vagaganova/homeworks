import time
from itertools import cycle


class TrafficLight:
    _color = None
    _colors = ['red', 'yellow', 'green']

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        el = 0
        for letter in cycle(self._colors):
            if el > 20:
                break
            self._color = letter
            print(self._color)
            if letter == self._colors[0]:
                time.sleep(7)
            elif letter == self._colors[1]:
                time.sleep(2)
            else:
                el += 1
                time.sleep(5)


traffic = TrafficLight()
traffic.running()