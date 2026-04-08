# TODO: Rendering (fml)

from bearlibterminal import terminal

class Renderer:

    def __init__(self, width=120, height=40):
        self._width = width
        self._height = height
        terminal.open()
        terminal.set(f"window: title='Inc', size={width}x{height}")
        terminal.set("font: default")
        self.running = True
        pass

    def render(self):
        while self.running:
            
            pass
    
    def split_view(self):
        
        pass

    def draw_box(self, x: int, y: int, w: int, h: int, title: str = ""):
        if x < 5:
            raise Exception('Box zu klein')

        if y < 5:
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

    def test_render(self):
        while True:
            terminal.clear()
            self.draw_box(10, 10, 10, 20, 'Svensonsonsonsonson')
            terminal.refresh()

if __name__ == '__main__':
    r = Renderer()
    r.test_render()
