# Controlling your mouse
# listening to your mouse
# Controlling your Keyboard
# listening to your keyboard - Will be finally in our keylogger

from pynput.mouse import Controller

def controlmouse():
    mouse = Controller()
    mouse.position = (10,20)

controlmouse()


# def controlkeyboard():
#     keyboard = Controller()
#     keyboard.type = ("I am freeking awesome!")

# controlkeyboard()





