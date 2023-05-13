import os
#import keyboard
import subprocess
#import pyautogui
import time
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

#Made by Fattcat with Love and hacking Skill #

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
print(f"{red}               .^^^^:  ::::::::^..::::::::^.                                    ")
sleep(0.2)
print(f"{red}             ~PPYJJ5Y :YYY5&GYY5~:YYYP&PYYY^                                    ")
sleep(0.2)
print(f"{red}             #&.          ^@J        ~@7         :!.:!77~.  ~~     :!.          ")
sleep(0.2)
print(f"{red}             !GGY7^       ^@J        !@7         7@P?!!7P#~ ?@!   .#P           ")
sleep(0.2)
print(f"{red}               :7YGG?     ^@J        !@7         !@7     #B  Y@^  GG            ")
sleep(0.2)
print(f"{red}                   ?@?    ^@J        !@7         !@7    :&P   PB.Y#.            ")
sleep(0.2)
print(f"{red}           .5Y?77JGG:    ^@J        !@7    .PY  !@GJ7!?GP:    G##:             ")
sleep(0.2)
print(f"{red}             :~!7!~:      .~:        .~.     !~  !@!:!!!:      J@~              ")
sleep(0.2)
print(f"{red}                                                 7@!        ~!YB~               ")
sleep(0.2)
print(f"{red}                                                :!.        ~7!.                ")
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
    def StartSound():
        sleep(0.3)
        os.system("start AuuughSound.mp3")
        sleep(3)
        print("Wait please ...")
        sleep(3)
        os.system("start AuuughSound.mp3")
        sleep(3)
        print(".")
        sleep(0.3)
        print("..")
        sleep(0.3)
        print("...")
        sleep(0.3)
        
    def helpCommands():
        print(f"'{green}-h{reset}' --> help")
        print(f"'{red}-e{reset}' --> Exit")
        d = input("Type : ")
        if d == "-h":
            os.system("clear")
            sleep(1)
            print("SOmething here")
            print
            sleep(1)
            os.system("clear")
        
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

    def DalsiSpustac():
        subprocess.call(["Piskotky.py"])
        # ESTE TO NENI CELE a ONO
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

    #def pygui():
        #for i in range(3):
            #sleep(1)
            #pyautogui.rightClick()
            #sleep(1)
            #pyautogui.mouseDown()
            #sleep(1)
            #pyautogui.mouseUp()
            #sleep(1)

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
    
    def WiFiKicker():
        print(f"{green}Starting{reset} {orange}WiFiKicker{reset}")
        sleep(1)
        subprocess.call([WiFiKicker.py])

    print(f"{green}[ 1 ]{reset} Start stt.py")
    print(f"{yellow}[ 2 ]{reset} Animation :D")
    print(f"{orange}[ 3 ]{reset} Select Language")
    print(f"{orange}[ 4 ]{reset} RE-INSTALL ALL PACKAGES")
    print(f"{red}[ 5 ]{reset} Exit")
    print(f"{green}[ -h ]{reset} Help")

    a = input(f"{blue}Select Option : {reset}")

    if a == "1":
        print("Loading ...")
        StartSound()
        #pygui()
    elif a == "2":
        print(f"{green}Starting ...\n{reset}")
        Animation()
        #if keyboard.is_pressed("ctrl", "c"):
            #print("BB YYY EEE")
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
