"""bearlibterminal Beispiel: Horizontale Zweiteilung.

Oben: ein grosses Feld.
Unten: 4 gleichgrosse Felder nebeneinander.
"""

from bearlibterminal import terminal


def draw_box(x: int, y: int, w: int, h: int, title: str = "") -> None:
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
    if title:
        label = f" {title} "
        terminal.printf(x + 2, y, label)


def draw_text_centered(x: int, y: int, w: int, h: int, text: str) -> None:
    """Zentriert einen Text innerhalb eines Bereichs."""
    tx = x + (w - len(text)) // 2
    ty = y + h // 2
    terminal.printf(tx, ty, text)


def main() -> None:
    terminal.open()
    terminal.set("window: title='Layout-Beispiel', size=80x25")
    terminal.set("font: default")

    width = 80
    height = 25
    split_y = height // 2  # Horizontale Teilung bei Zeile 12

    # Hoehen
    top_h = split_y + 1        # obere Haelfte (inkl. Trennlinie)
    bot_h = height - split_y   # untere Haelfte
    panel_w = width // 4       # Breite jedes unteren Panels

    running = True
    while running:
        terminal.clear()

        # === Oberes grosses Feld ===
        draw_box(0, 0, width, top_h, "Hauptbereich")
        draw_text_centered(0, 0, width, top_h, "Hier ist der grosse obere Bereich")

        # === Untere 4 Felder ===
        panel_titles = ["Panel 1", "Panel 2", "Panel 3", "Panel 4"]
        for i in range(4):
            px = i * panel_w
            draw_box(px, split_y, panel_w, bot_h, panel_titles[i])
            draw_text_centered(px, split_y, panel_w, bot_h, f"Feld {i + 1}")

        terminal.refresh()

        # Event-Loop
        key = terminal.read()
        if key in (terminal.TK_CLOSE, terminal.TK_ESCAPE, terminal.TK_Q):
            running = False

    terminal.close()


if __name__ == "__main__":
    main()
