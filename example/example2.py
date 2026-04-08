import keyboard


thing = 'a'

def bar():
    global thing
    thing = 'b'
    print('b')

def foo():
    global thing
    keyboard.on_release_key('a', bar)
    while True:
        # print(thing)
        pass

if __name__ == '__main__':
    foo()
