from player import Player
from factory import Factory
from keyboard import keyboard
from datetime import datetime

TICK_TIME = .05

class Game:
    _last_tick_time = None
    def __init__(self):
        self._active = False
        self.factory = Factory('Fact', 10, 1, 1, 10)
        self.money = 0

    def start(self):
        self._active = True
        self._run()
        pass

    def run(self):
        self._last_tick_time = datetime.now()
        while self._active:
            # TODO:
            self.tick()
        pass

    def render(self):

        pass

    def handle_input(self):
        
        if keyboard.is_pressed('b'):
            self.buy()

        pass

    def buy(self):
        # TODO:
        pass

    def pause(self, index):

        pass

    def tick(self):
        self.handle_input()
        self.money += self.factory.tick()
        pass
