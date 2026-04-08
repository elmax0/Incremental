import keyboard

pressed = False
def test():
    global pressed
    while True:
        
        if keyboard.is_pressed('q'):
            break
        elif keyboard.is_pressed('a'):
            if not pressed:
                print('a')
            pressed = True
        else:
            pressed = False
    pass

if __name__ == '__main__':
    test()
