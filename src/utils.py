from enum import Enum:

class State(Enum):
    MENU = 1
    GAME = 2
    PAUSE = 3
    SHOP = 4


class GameState:
    state: State = State.MENU
    data = None
    def __init__(self):

        pass

    def pause(self):
        if self.state == State.MENU:
            self.state = State.GAME
            return
        self.state = State.MENU

    def start(self):
        if self.state == State.MENU:
            self.state = State.GAME


