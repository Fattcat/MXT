import os
from time import sleep
import subprocess
import shutil
import sys
import random

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
#orange = '\033[033m'
P = '\033[15m'  # purple
orange = '\033[38;5;208m'
magenta = '\033[35m'
cyan = '\033[36m'
reset = '\033[0m'

Words = ["Ohh", "More sak", "Ciii Kokiiii", "Fuuha", "xD", "LoL"]
RanGenerated = random.choice(Words)

for i in range(99):
    print(RanGenerated + "Neni dokonceny")
    sleep(0.01)
    print(i)
    sleep(0.1)
    if i > 90:
        print("LOL...")