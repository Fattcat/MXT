import os
import keyboard
import subprocess
import pyautogui
import time
from time import sleep
import random

#Made by Fattcat with Love and hacking Skill #

list = ("red", "green", "yellow", "blue", "orange")

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
#orange = '\033[033m'
orange = '\033[38;5;208m'
magenta = '\033[35m'
cyan = '\033[36m'
reset = '\033[0m'

print(f'{red}{green}Hello, world!{reset}')

os.system("clear")
print("-------------------------------------------------------------------------\n")
sleep(0.3)
print(f"/////////////////////////// {blue}WELCOME TO{reset} {red}stt.py{reset} ///////////////////////////")
print(f"///////////////////////////   {green}Version 1.0.0{reset}   ///////////////////////////")
sleep(0.3)
print(f"////////////////////////// Created By Fattcat ///////////////////////////\n")
sleep(0.3)
print(f"/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\{green}- ENGLISH -{reset}/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ \n")
sleep(0.3)
print("-------------------------------------------------------------------------\n")
sleep(1)

while True:

    def LangEN():
        os.system("clear")

        # TREBA DOROBIT

    def LangSK():
        os.system("clear")
        
        # TREBA DOROBIT

    def Languages():
        os.system("clear")
        sleep(1)
        print("")
        print("\n")
        print(f"{orange}[ 1 ]{reset} {green}English{reset}")
        print(f"{orange}[ 2 ]{reset} {green}Slovak{reset}")
        print(f"{red}[ 3 ]{reset} {green}EXIT{reset}")
        print("")
        print("\n")
        c = input(f"{blue}Pick : {reset}")
        if c =="1":
            os.system("clear")
            sleep(1)
            #LangEN()
        elif c =="2":
            os.system("clear")
            sleep(1)
            #LangSK()
        elif c =="3":
            exit

    def Animation():
        subprocess.call(["python", "animation.py"])

    def REINSTALL():
        print("INSTALLING ALL PACKAGES ...\nPLEASE WAIT ...\n")
        sleep(1)
        subprocess.run(["pip", "install", "os"])
        sleep(1)
        subprocess.run(["pip", "install", "pyautogui"])
        sleep(1)
        subprocess.run(["pip", "install", "pywifi"])
        sleep(1)
        os.system("clear")
        print(f"{green} ( -- INSTALLATION COMPLETED -- ){reset}\n")
        sleep(1)
        os.system("clear")

    def BYEBYE():
        print("")
        print("")
        print(f"        {blue}+--------------------------------------------+{reset}")
        print(f"              |            {yellow}BYE BYE              {reset}|")
        print(f"              |  {green}Thank You for using stt.py{reset}     |")
        print(f"        {blue}+--------------------------------------------+{reset}")
        print("")
        print("")
        sleep(2)
        os.system("clear")
        exit()

    def pygui():
        for i in range(3):
            sleep(1)
            pyautogui.rightClick()
            sleep(1)
            pyautogui.mouseDown()
            sleep(1)
            pyautogui.mouseUp()
            sleep(1)

    def iwconfig():
        print("Starting IWCONFIG ...\n")
        sleep(1)
        os.system("iwconfig")

    def MonitorModeWlan1UP():
        print("Starting airmon-ng on 'wlan1'")
        os.system("sudo airmon-ng check")
        sleep(0.1)
        os.system("sudo airmon-ng check kill")
        sleep(0.1)
        os.system("sudo airmon-ng start wlan1")
        sleep(0.1)

    def MonitorModeWlan1DOWN():
        print("Starting airmon-ng on 'wlan1'")
        os.system("sudo airmon-ng check")
        sleep(0.1)
        os.system("sudo airmon-ng check kill")
        sleep(0.1)
        os.system("sudo airmon-ng start wlan1")
        sleep(0.1)

    print(f"{green}[ 1 ]{reset} Start stt.py")
    print(f"{yellow}[ 2 ]{reset} Animation :D")
    print(f"{orange}[ 3 ]{reset} Select Language")
    print(f"{orange}[ 4 ]{reset} RE-INSTALL ALL PACKAGES")
    print(f"{red}[ 5 ]{reset} Exit")

    a = input("Select Option : ")

    if a == "1":
        print("Loading ...")
        pygui()
    elif a == "2":
        print(f"{green}Starting ...\n{reset}")
        Animation()
        if keyboard.is_pressed("ctrl", "c"):
            print("BB YYY EEE")
        #subprocess.Popen("am start -n com.android.chrome/com.google.android.apps.chrome.Main", shell=True)
    elif a == "3":
        Languages()
        print(f'{green}Starting ...\n{reset}')
    elif a == "4":
        print(f'{red}Starting ...\n{reset}')
        REINSTALL()
    elif a == "5":
        os.system("clear")
        sleep(0.3)
        BYEBYE()
    else:
        b = input("Press Y to restart stt.py OR Press N for exit : ")
        if b =="Y" or b =="y":
            continue
        elif b =="N" or b =="n":
            print("bye :D")
            BYEBYE()
        else:
            print(f"{red}       Wrong Input ! Cancelling ...{reset}")
            sleep(1)
            break
