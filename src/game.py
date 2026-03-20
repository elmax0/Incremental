from player import Player
from factory import Factory

class Game:
    def __init__(self):
        self._active = False
        self.factory = Factory('Fact', 10, 1, 1, 10)
        self.money = 0

    def start(self):
        self._active = True
        self._run()
        pass

    def run(self):
        while self._active:
            # TODO:
            self.handle_input()
            self.tick()
        pass

    def render(self):

        pass

    def handle_input(self):
        
        pass

    def buy(self, index):
        # TODO:
        pass

    def pause(self, index):

        pass

    def tick(self):
        self.money += self.factory.tick()
        pass