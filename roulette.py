import random
from collections import deque  
import sys
import subprocess

chamber = [False]*5 + [True]
random.shuffle(chamber)
gun = deque(chamber)

# print(gun)

while True:
    play = input("Do you want to pull the trigger?'n' to quit 'enter' to continue")
    if play.lower() == 'n':
        break
    else:
        if gun[0]:
            print('BANG')
            start_again = input("Do you want to start again? (y/n): ")
            if start_again and start_again.lower()[0] == "y":
             subprocess.call([sys.executable, sys.argv[0]])
             break
            else:
             break
        else:
            print('click')
            gun.rotate(-1) 
