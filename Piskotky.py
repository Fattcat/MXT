import os
import datetime
from time import sleep
import random

# VERSION 1.0.0
# Date 11.06.2023

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
#orange = '\033[033m'
orange = '\033[38;5;208m'
magenta = '\033[35m'
cyan = '\033[36m'
reset = '\033[0m'

def EXIT():
    sleep(0.2)
    print(f"      {green}+{reset} ---------------------------- {green}+{reset}")
    print(f"      {orange}|{reset}          {red}EXITTING{reset} ...        {orange}|{reset}")
    print(f"      {green}+{reset} ---------------------------- {green}+{reset}")
    sleep(2)
    os.system("clear")
    exit()

def BigCookie():
    print("""
    
    
    @@@@@@@@@@@@@@@@@@@@@@@@&&##BBBB##&&@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@&BPY?7!!~~~~~~~~?&@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@&GY7~~^^^^~~~~~~~~^!#@@@@@@@@@@@&##@@@@@@@@@@@
    @@@@@@@@@@@&GJ!^^^~~~~~~^^~~~~~~^G@@@@@@@@@P?7!~~Y@@@@@@@@@@
    @@@@@@@@@Y7!^^~~~~~~~~^?GJ~~~~~~!&@@@@@@@@B~^^^~^5@@@@@@@@@@
    @@@@@@@&Y^^~~~~~~~~~~~~!5P!~~~~^7@@@@@@@@@&Y7!~~7&@@@@@@BP&@
    @@@@@@B!^~~~~~^^^^^^~~~~^^~^~~~~~#@@@@@@@@@@@&BB&@@@@@@@GY&@
    @@@@@5~^~~~~^~?5P5Y7~~~~~~^J#P~~^J@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@Y~~~~~~^7#&PY5G&G!~~~~~7?~~~~^5@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@5~~~~~~~^B@J777!5@Y^~~~~^^^^~~~^J#@@@@@@@@@@@@@G?!?B@@@@@
    @@B!~~~~~~~^J@B5JJ5&#7^~~~~?55?~~~~^~Y#@@@@@@@@@@@B!~7B@@@@@
    @@J~~~~~~~~~^75GBBGY~^~~~^5@GP@G^~~~~^~?P#&@@@@@@@@&B@@@@@@@
    @&!!~~~~~~~^~^^^~~^^~~~~~^?#BB#J^~~~~~~^^~!?J5#@@@@@@@@@@@@@
    @B!!~~~~^J#?~~~~~~~~~~^^~~^~!7~^~~~~^^^~~~~^^^!B@@@@@@@@@@@@
    @B!!~~~~~~GB~~~~~~~~~!P?~~~~~^~~~~~~7Y5!~~~~~~^~5&@@@@@@@@@@
    @&!!!~~~~~^~~~~~~^^^^!5G!~~~~~~~~~~!GPJ~~~~~~^^~^~JP#&@@@@@@
    @@J~!~~~~~~~~~~^!?JJ7^^^~~~~~~~~~~^^^^^^~~~~~??^~~^^~!!77Y@@
    @@B!!!~~~~~~~~~Y&BPG&B!~~~~~~~~~^~?Y5Y?!^~~~~5@Y^~~~~~^^^B@@
    @@@5~!!~~~~~~~~&@J77P@J^~~~~~~~^J##P5PB&Y~~~~~??~~~~~~~^5@@@
    @@@@Y~!!~~~~~~~?B#BB#5~~~~~~~~~!@&?77!!B@7^~~~^^~~~~~~^J@@@@
    @@@@@5~~!!~~~~~^~!7!~^~^^^~~~~~~G@PYJJ5&B~~~~~~~~~~~^^Y@@@@@
    @@@@@@G7~!!~~~~~~~^~~~~7Y5~~~~~~~JGBBBGJ~~~~~~~~~~~^!G@@@@@@
    @@@@@@@&5!~~!~~~~~~~~^7GPJ~~~~~~~^^~~~^^~~~~~~~~~^^Y&@@@@@@@
    @@@@@@@@@&57~~!!~~~~~~~^^^~~~~~~~J7~~~~~~~~~~~^^!7J@@@@@@@@@
    @@@@@@@@@@@&GJ!~~~~~~~~~~~~~~~~~!#5^~~~~~~^^~!JG&@@@@@@@@@@@
    @@@@@@@@@@@@@@&GY?!!~~~~~~~~~~~~~~~~~~~~~!?YG&@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@&BP5J?77!!!!!!!!77?J5PB&@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@&&########&&@@@@@@@@@@@@@@@@@@@@@@@@
    
    
    """)


os.system("clear")

print("\n")
print("\n")
print(f"                  {red}PisKoTKy{reset} \n")
print(f"{green}Welcome to PisKoTKy{reset} A.K.A. Fake cookie Stealer")
BigCookie()

print(f"[ {green}1{reset} ] --> {orange}Start {reset}")
print(f"[ {green}2{reset} ] --> {orange}Start {reset}")
print(f"[ {green}3{reset} ] --> {orange}Start {reset}")
print(f"[ {green}4{reset} ] --> {orange}Start {reset}")
print(f"[ {green}5{reset} ] --> {orange}Start {reset}")
print(f"[ {red}99{reset} ] --> {red}EXIT{reset}")
print("\n")
FirstChoice = input(f"{yellow}-->{reset} ")

if FirstChoice =="1":
    print(f"{green}Starting{reset} nieco ...")

elif FirstChoice =="2":
    print(f"{green}Starting{reset} nieco ...")

elif FirstChoice =="3":
    print(f"{green}Starting{reset} nieco ...")

elif FirstChoice =="4":
    print(f"{green}Starting{reset} nieco ...")

elif FirstChoice =="5":
    print(f"{green}Starting{reset} nieco ...")

elif FirstChoice =="6":
    EXIT()
else:
    print("Bad INPUT number")
    sleep(1)
    EXIT()
