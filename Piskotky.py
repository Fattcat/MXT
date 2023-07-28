import os
import datetime
from time import sleep
import random
#from selenium import webdriver

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

def ChromeCookStealer():
        # Launch Chrome browser
    driver = webdriver.Chrome()

    # Open a website
    driver.get("https://www.example.com")

    # Find and interact with elements on the page
    element = driver.find_element_by_id("myElement")
    element.click()

    # Extract information from the page
    text = driver.find_element_by_css_selector(".myClass").text
    print(text)

    # Close the browser
    driver.quit()

os.system("clear")

print("\n")
print("\n")
print(f"                           {red}PisKoTKy{reset} \n")
print(f"{green}         Welcome to PisKoTKy{reset} A.K.A. Fake cookie Stealer")
BigCookie()

print(f"[ {orange}1{reset} ] --> {green}Start {orange}Chrome{reset} Cookie Stealer")
print(f"[ {orange}2{reset} ] --> {green}Start {orange}Microsoft{reset} Edge Cookie Stealer{reset}")
print(f"[ {orange}3{reset} ] --> {green}Start {orange}Firefox{reset} Cookie Stealer{reset}")
print(f"[ {orange}4{reset} ] --> {green}Start {orange}Opera{reset} Cookie Stealer{reset}")
print(f"[ {orange}5{reset} ] --> {green}Select WHERE You want TO SAVE Output{reset}")
print(f"[ {red}99{reset} ] --> {red}EXIT{reset}")
print("\n")
FirstChoice = input(f"{yellow}      ----->{reset} ")

if FirstChoice =="1":
    print(f"{green}Starting{reset} ChromeCookStealer ...")
    ChromeCookStealer()

elif FirstChoice =="2":
    print(f"{green}Starting{reset}Chrome C.S. ...")

elif FirstChoice =="3":
    print(f"{green}Starting{reset}Microsoft Edge C.S. ...")

elif FirstChoice =="4":
    print(f"{green}Starting{reset}Opera C.S. ...")

elif FirstChoice =="5":
    print(f"{green}Starting{reset} SeTTinGZ ...")

elif FirstChoice =="99":
    EXIT()
else:
    print("       + ----------------------- +")
    print("       + - Wrong INPUT number  - +")
    print("       + ----------------------- +")
    sleep(1)
    EXIT()
