import os
from time import sleep
import subprocess
import shutil
import sys
import random
import getpass

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

meno = getpass.getuser()
words = ["Whats up Dude", "Hello", "Hi"]
ranGen = random.choice(words)
print(ranGen, (meno), "THIS IS WormCreator.py POWERFUL PYTHON SCRIPT")
