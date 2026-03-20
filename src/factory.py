from decimal import decimal 

class Factory:
    def __init__(self, name, health, cash, cash_per_second, upgrade_cost, level: int = 1, active: bool = False):
        self._name = name
        self._max_health = health
        self._health = health
        self._cash = cash
        self._cash_per_second = cash_per_second
        self._upgrade_cost = upgrade_cost
        self._initial_upgrade_cost = upgrade_cost
        self._active = active
        self._level = level
        self._running = False
        pass

    def tick(self, timedelta: float) -> float:
        if not self._running:
            return 0.0
        return self._cash_per_second * timedelta
    
    def click(self, damage) -> float:
         self._health -= damage
         if self._heatlh <= 0.0:
             self._health = self._max_health
             return self._cash
         return 0.0
    
    def upgrade(self):
        self._max_health *= 1.5
        self._health = self._max_health
        self._cash *= 1.5
        self._upgrade_cost *= 1.5
        pass

    @property
    def stats(self):
        return f'{self._health} / {self._max_health}'

    