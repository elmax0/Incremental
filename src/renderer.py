# TODO: Rendering (fml)

from bearlibterminal import terminal
from factory import Factory
from character import Character


class Renderer:

    def __init__(self, width=120, height=80):
        self._width = width
        self._height = height
        terminal.open()
        terminal.set(f"window: title='Inc', size={width}x{height}")
        terminal.set("font: default")
        self.running = True
        pass

    def render(self, game_state):
        switch(game_stat)
        fac_data = game_state[0]
        box_data = [] 
    
    def draw(self, fac_data, box_data):
        # data -> [1 upper, 4 boxes]
        self.draw_fac(fac_data)
        self.draw_boxes(box_data)
        pass

    def draw_fac(self, factory):
        # Box mit Namen
        self.draw_box(0, 0, self._width, int(self._height/2), factory._name)
        
        # Stats
        terminal.printf(1, 2, factory.stats)
        terminal.printf(1, 3, str(factory._cash))
        terminal.printf(1, 4, str(factory._upgrade_cost))
        terminal.printf(1, 5, f'DPS: {factory._cash_per_second}')
        pass

    def draw_character(self, x: int, y: int, w: int, h: int, char: Character = Character("Template")):
        if w < 5:
            raise Exception('Box zu klein')

        if h < 5:
            raise Exception('Box zu klein')
        # Text abgefangen
        if w < len(char.name):
            w = len(char.name) + 4

        # Ecken
        terminal.put(x, y, 0x250C)
        terminal.put(x + w - 1, y, 0x2510)
        terminal.put(x, y + h -1, 0x2514)
        terminal.put(x + w -1, y + h -1, 0x2518)

        # Horiz
        for i in range(1, w - 1):
            terminal.put(x + i, y, 0x2500)
            terminal.put(x + i, y + h - 1, 0x2500)

        # Vert
        for j in range(1, h-1):
            terminal.put(x, y + j, 0x2502)
            terminal.put(x + w - 1, y + j, 0x2502)

        if char:
            label = f" {char.name} "
            diff = int((w - len(label))/2)
            terminal.printf(x + diff, y, label)
            diff = int((w - len(char.health))/2)
            terminal.printf(x + diff, y+1, char.health)
            for i in range(char.get_values()):
                
                pass
        pass
 
    def draw_box(self, x: int, y: int, w: int, h: int, title: str = ""):
        if w < 5:
            raise Exception('Box zu klein')

        if h < 5:
            raise Exception('Box zu klein')
        # Text abgefangen
        if w < len(title):
            w = len(title) + 4

        # Ecken
        terminal.put(x, y, 0x250C)
        terminal.put(x + w - 1, y, 0x2510)
        terminal.put(x, y + h -1, 0x2514)
        terminal.put(x + w -1, y + h -1, 0x2518)

        # Horiz
        for i in range(1, w - 1):
            terminal.put(x + i, y, 0x2500)
            terminal.put(x + i, y + h - 1, 0x2500)

        # Vert
        for j in range(1, h-1):
            terminal.put(x, y + j, 0x2502)
            terminal.put(x + w - 1, y + j, 0x2502)

        if title:
            label = f" {title} "
            diff = int((w - len(label))/2)
            terminal.printf(x + diff, y, label)
        pass
    
    def draw_boxes(self, box_data):
        for i in range(4):
            self.draw_character(i*30, 40, 30, 40, box_data[i])

        pass

    def test_render(self):
        while True:
            terminal.clear()
            # self.draw_box(10, 10, 10, 20, 'Svensonsonsonsonson')
            self.draw_boxes()
            terminal.refresh()

    def test_render2(self, factory : Factory):
        boxes = [ Character('Dieter'),  Character('Vieter') ,  Character('Tieter') ,  Character('Pieter')]
        while True:
            terminal.clear()
            self.draw(factory, boxes)
            terminal.refresh()
        pass

if __name__ == '__main__':
    factory = Factory('factory', 100, 10, 0, 10)
    r = Renderer()
    r.test_render2(factory)
