import os
import datetime
from time import sleep
import random

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
#orange = '\033[033m'
orange = '\033[38;5;208m'
magenta = '\033[35m'
cyan = '\033[36m'
reset = '\033[0m'

def Piskota1():
  random.choice(red, green, yellow, blue, orange, magenta, cyan)
  
print(f"//////////// {red}PisKoTKyY{reset} \\\\\\\\\\\\\n")
print(f"{green}Welcome to Piskotky{reset}")
