from decimal import decimal 

class Factory:
    def __init__(self, name, cash, cash_per_second, upgrade_cost, active: bool = False):
        self._name = name
        self._cash = cash
        self._cash_per_second = cash_per_second
        self._upgrade_cost = upgrade_cost
        self._initial_upgrade_cost = upgrade_cost
        self._active = active
        pass

    def tick(self, timedelta: float) -> float:
        if not self._active:
            return 0.0
        return self._cash_per_second * timedelta
