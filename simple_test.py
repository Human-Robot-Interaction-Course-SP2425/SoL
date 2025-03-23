from time import sleep
from utils import *
import keyboard

init_robot()

# run_seq("reset")
# sleep(1)
# run_seq("yes")
# sleep(5)
# run_seq("happy")
# sleep(5)
# run_seq("sad")
# sleep(10)
# run_seq("happyyyy")
# sleep(10)


while True:
    try:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:  
            if event.name == 'left':
                print("left")
                run_seq("left")
                sleep(1)
            elif event.name == 'right':
                print("right")
                run_seq("right")
                sleep(1)
            elif event.name == 'down':
                print("down")
                run_seq("down")
                sleep(1)
            elif event.name == 'up':
                print("up")
                run_seq("up")
                sleep(1)
            elif event.name == 'r':
                print("reset")
                run_seq("reset")
                sleep(1)
            elif event.name == 'space':
                print("space")
                run_seq("hungry")
                sleep(1)
    except KeyboardInterrupt:
        break
