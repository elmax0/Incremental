

class Player:
    def __init__(self, damage=1):
        self._damage = damage
        pass

    def hit(self) -> float:
        return self.damage
    
