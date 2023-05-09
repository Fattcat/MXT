import os
import subprocess
import pyautogui
import time
from time import sleep

#Made by Fattcat with Love and hacking Skill #

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
orange = '\033[33m\033[31m'
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

    def REINSTALL():
        subprocess.run[("pip","install")]

    def pygui():
        for i in range(3):
            pyautogui.click("right")
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
        print(f'{green}helloooo mONEEE\n{reset}')
        subprocess.Popen("am start -n com.android.chrome/com.google.android.apps.chrome.Main", shell=True)
    elif a == "3":
        print(f'{green}helloooo mONEEE\n{reset}')
    elif a == "4":
        print(f'{red}helloooo mONEEE\n{reset}')
    elif a == "5":
        os.system("clear")
        sleep
        print(f'{yellow}Bye bye\n{reset}')
        sleep(2)
        os.system("clear")
        exit()
    else:
        b = input("Press Y to restart stt.py OR Press N for exit : ")
        if b =="Y":
            continue
        elif b =="N":
            print("bye :D")
        else:
            break
