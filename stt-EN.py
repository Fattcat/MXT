import os
#import keyboard
import subprocess
import time
from time import sleep
import random
#from playsound import playsound
#import pywifi
#import pygame

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

# Made by Fattcat with Love and hacking Skill #
# LAST UPDATED and add sme Features with PROGRAMS : 29.05.2023

pozdravy = ("Hello", "Hi", "Whats Up Dude", "Stay Free", "PROFESSIONAL")

print(f'{red}Hello, world!{reset}')

os.system("clear")
sleep(1)
print("                                                                                 ")
sleep(1)
print("                                                                                 ")
sleep(0.2)
print("                                                                                 ")
sleep(0.2)
print("                                                                                 ")
sleep(0.2)
print(f"{red}               .^^^^:  ::::::::^..::::::::^.                                    {reset}")
sleep(0.2)
print(f"{red}             ~PPYJJ5Y :YYY5&GYY5~:YYYP&PYYY^                                    {reset}")
sleep(0.2)
print(f"{red}             #&.          ^@J        ~@7         :!.:!77~.  ~~     :!.          {reset}")
sleep(0.2)
print(f"{red}             !GGY7^       ^@J        !@7         7@P?!!7P#~ ?@!   .#P           {reset}")
sleep(0.2)
print(f"{red}               :7YGG?     ^@J        !@7         !@7     #B  Y@^  GG            {reset}")
sleep(0.2)
print(f"{red}                   ?@?    ^@J        !@7         !@7    :&P   PB.Y#.            {reset}")
sleep(0.2)
print(f"{red}           .5Y?77JGG:    ^@J        !@7    .PY  !@GJ7!?GP:    G##:             {reset}")
sleep(0.2)
print(f"{red}             :~!7!~:      .~:        .~.     !~  !@!:!!!:      J@~              {reset}")
sleep(0.2)
print(f"{red}                                                 7@!        ~!YB~               {reset}")
sleep(0.2)
print(f"{red}                                                :!.        ~7!.                {reset}")
sleep(0.2)
print("                                                                                ")
sleep(0.2)
print("                                                                                ")
sleep(2)


os.system("clear")
print("+-------------------------------------------------------------------------+\n")
sleep(0.3)
print(f"|/////////////////////////// {blue}WELCOME TO{reset} {red}stt.py{reset} ///////////////////////////|")
print(f"|///////////////////////////   {green}Version 1.0.0{reset}   ///////////////////////////|")
sleep(0.3)
print(f"|////////////////////////// Created By Fattcat ///////////////////////////|\n")
sleep(0.3)
print(f"|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\{green}- ENGLISH -{reset}/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|\n")
sleep(0.3)
print("                      ",random.choice(pozdravy),"(Random Generated)\n")
print("+-------------------------------------------------------------------------+\n")
sleep(1)

while True:
    def StartScan():
        os.system("clear")
        sleep(1)
        print("NENI TO DOKONCENE MA TO SPUSTIT WiFi SCANNER")
        #os.system("")
        
    def helpCommands():
        print(f"'{green}-h{reset}' --> help")
        print(f"'{red}-e{reset}' --> Exit")
        d = input("Type : ")
        if d == "-h":
            os.system("clear")
            sleep(1)
            print(f"- {green}Help Centre{reset} -\n")
            print("Option 1 is for Start WiFi Scanner")
            print("Option 2 is for Start Kicking users from Routers Around You\n(YOU NEED TO WRITE Yes for start it without problems)")
            print("Option 3 is for Start Script to Capture Cookies on browsers : (Chrome, Edge, FireFox, Brave)")
            print("Option 4 is for Start Script to Capture WiFi Hand Shake")
            print("Option 5 is for running an unfinished script")
            print("Option 6 is for Start Animated smile")
            print("Option 7 is for Selecting Languages (EN, SK, CZ, FR, ...)")
            print("Option 8 is for RE-Installing necessary files and programs\n")
            input("PRESS ANY KEY FOR CONTINUE ")

        
        elif d =="-e":
            print("Exitting ...")
            sleep(1)
            BYEBYE()
        else:
            breake
    def LangEN():
        os.system("clear")
        sleep(1)
        print("+-------------------------+")
        print(f"| Language mode : {green}English{reset} |")
        print("+-------------------------+")
        sleep(1)
        print(f"{green}Dude, SORRY this is not set{reset}")
        sleep(3)
        os.system("clear")
        sleep(1)
        # TREBA DOROBIT

    def LangSK():
        os.system("clear")
        sleep(1)
        print("+-------------------------+")
        print(f"| Language mode : {green}Slovak{reset}  |")
        print("+-------------------------+")
        sleep(1)
        print(f"{green}Kaamo, PREPAC neni to dorobenee{reset}")
        sleep(3)
        os.system("clear")
        sleep(1)
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
            LangEN()
        elif c =="2":
            os.system("clear")
            sleep(1)
            LangSK()
        elif c =="3":
            BYEBYE()
            sleep(2)
        else:
            print("Wrong Input")

    def Animation():
        #subprocess.call(["python", "animation.py"])
        os.system("python3 Piskotky.py")
    def REINSTALL():
        print("INSTALLING ALL PACKAGES ...\nPLEASE WAIT ...\n")
        sleep(1)
        subprocess.run(["pip","install ","playsound"])
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
    
    def KickerFi():
        print(f"{green}Starting{reset} {orange}KickerFi{reset}")
        sleep(1)
        #subprocess.call([KickerFi.py])
        os.system("python3 KickerFi.py")
    def Piskotky():
        #subprocess.call([Piskotky.py])
        os.system("clear")
        os.system("python3 Piskotky.py")
    print(f"{green}[ 1 ]{reset} Start stt.py")
    print(f"{green}[ 2 ]{reset} Start KickerFi.py")
    print(f"{green}[ 3 ]{reset} Start Piskotky.py")
    print(f"{green}[ 4 ]{reset} Start Capture WiFi HandShake")
    print(f"{green}[ 5 ]{reset} Start SomeScript.py")
    print(f"{yellow}[ 6 ]{reset} Animation :D")
    print(f"{orange}[ 7 ]{reset} Select Language")
    print(f"{orange}[ 8 ]{reset} RE-INSTALL ALL PACKAGES")
    print(" ")
    print(f"{red}[ 9 ]{reset} Exit")
    print(f"{green}[ -h ]{reset} Help")
    print(" ")
    a = input(f"{blue}Select Option : {reset}")

    if a == "1":
        print("Loading ...")
        StartScan()
        print("Neni to FUNKCNE ...")
        
    elif a == "2":
        print(f"{green}Starting ... {blue}KickerFi{reset}\n{reset}")
        sleep(1)
        KickerFi()

    elif a == "3":
        print(f'{green}Starting ...\n{reset}')
        sleep(1)
        os.system("python Piskotky.py")
    elif a == "4":
        print(f'{red}Starting ...\n{reset}')
        sleep(1)
        REINSTALL()

    elif a == "5":
        print(f'{green}Starting ...\n{reset}')
        sleep(1)
        
    elif a == "6":
        print(f'{green}Starting ...\n{reset}')
        sleep(1)
        Animation()
    elif a == "7":
        print(f'{green}Starting ...\n{reset}')
        sleep(1)
        Languages()

    elif a == "8":
        os.system("clear")
        sleep(0.3)
        print("Starting RE-Installing all Necessary files ...")
        sleep(0.3)
        REINSTALL()
    
    elif a == "9":
        exit()
        print(f'{green}Starting ...\n{reset}')

    elif a =="-h":
        helpCommands()
    else:
        b = input(f"Press {green}Y{reset} to restart stt.py OR Press {red}N{reset} for exit : ")
        if b =="Y" or b =="y" or b =="yes" or b =="Yes":
            continue
        elif b =="N" or b =="n" or b =="No" or b =="no":
            print("\n\n                          bye :D\n")
            BYEBYE()
        else:
            print(f"{red}       Wrong Input ! Cancelling ...{reset}")
            sleep(1)
            break
