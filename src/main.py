import tcod

WIDTH = 1200
HEIGHT = 800

console = tcod.Console(WIDTH, HEIGHT)


def main():
    with tcod.context.new_terminal(WIDTH, HEIGHT, title="Hello TCOD") as context:
        console.print(1, 1, "Hello world!")

        context.present(console)

        # wait until window closes
        while True:
            for event in tcod.event.wait():
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()

    pass


if __name__ == '__main__':
    main()
