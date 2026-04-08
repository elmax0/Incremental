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
        if self._level > 10:
            if self._cash_per_second == 0:
                self._cash_per_second = 1.5
                return
            self._cash_per_second *= 2
    

    @property
    def stats(self):
        return f'{self._health} / {self._max_health}'
    
    def render(self, terminal, x, y, w, h):
        """Zeichnet eine Box mit optionalem Titel."""
        # Ecken
        terminal.put(x, y, 0x250C)              # ┌
        terminal.put(x + w - 1, y, 0x2510)      # ┐
        terminal.put(x, y + h - 1, 0x2514)      # └
        terminal.put(x + w - 1, y + h - 1, 0x2518)  # ┘

        # Horizontale Linien
        for i in range(1, w - 1):
            terminal.put(x + i, y, 0x2500)          # ─
            terminal.put(x + i, y + h - 1, 0x2500)

        # Vertikale Linien
        for j in range(1, h - 1):
            terminal.put(x, y + j, 0x2502)          # │
            terminal.put(x + w - 1, y + j, 0x2502)

        # Titel
        if self._name:
            label = f" {self._name} "
            terminal.printf(x + 2, y, label)
        pass
    
