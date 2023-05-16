import os
import subprocess
from time import sleep
import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
#orange = '\033[033m'
orange = '\033[38;5;208m'
magenta = '\033[35m'
cyan = '\033[36m'
reset = '\033[0m'

def exitting():
    print(" ")
    print(" ")
    print("Exitting ...")

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

def Start_KickerFi():
    os.system("clear")
    print(" ")
    print(" ")
    print(f"           {yellow}PLUG IN{reset} Your WiFi Adapter")
    print(" ")
    print(" ")
    sleep(3)
    a = input(f"Type {green}Y{reset} for {green}START{reset} or {red}C{reset} for {red}CANCEL{reset} : ")
    if a =="y" or a =="Y":
        MonMODE_wlan1()
        print(" ")
        print(" ")
        print(f"[ 0 ] {green}START nieco co este NENI{reset} ")
        print(f"[ 1 ] {red}STOP{reset} {orange}MONITOR MODE on 'wlan1'{reset}")
        print(f"[ 2 ] {red}STOP{reset} {orange}MONITOR MODE on 'wlan0'{reset}")
        print(f"[ 3 ] {red}EXIT{reset}")
        c = input("Option : ")
        if c =="0":
            os.system("clear")

        elif c =="1":
            os.system("clear")    
            sleep(1)
            os.system("sudo airmon-ng wlan1 stop")
            sleep(3)
            os.system("sudo service NetworkManager restart")
            sleep(1)
        elif c =="2":
            os.system("clear")    
            sleep(1)
            os.system("sudo airmon-ng wlan0 stop")
            sleep(3)
            os.system("sudo service NetworkManager restart")
            sleep(1)
            print(f"{orange}MONITOR MODE{reset} {green}DISABLED{reset} ...")
            print("\n")
        elif c =="3":
            exitting()
        
        else: 
            print("Invalid input")
            exitting()
    
    elif a =="c"or a =="C":
        print("Bye Bye :D")
        exitting()
    print("")
    print("")


def SetupKickerFi():
    os.system("clear")

print("Starting ... to co neno nastavene")
os.system("clear")
sleep(1)
print(" ")
print(" ")
print(f"-------------------------------------------------")
print(f"{blue}        (--)                         (--)        {reset}")
print(f"------({green}O{reset}-__-{green}O{reset})                     ({green}O{reset}-__-{green}O{reset})------{reset}")
print(f"         {green}/\{reset}                           {green}/\{reset}         ")
print(f"        :  :    Welcome to {red}KickerFi{reset}  :  :        ")
print(f"------({green}O{reset}-__-{green}O{reset})                     ({green}O{reset}-__-{green}O{reset})------{reset}")
print(f"{blue}        (--)                         (--)        {reset}")
print(f"-------------------------------------------------")
print(" ")
print(" ")
sleep(2)
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
print("""                                                    .!:
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
                           .~77!^                        """)
print("                                                    ")
print("                                                    ")
sleep(2)
os.system("clear")

print(" ")
print(f"{green}[ 1 ]{reset} {green}START KickerFi{reset} KICK ALL DEVICES on ALL WiFi Routers around 6 to 33 meters")
print(f"{magenta}[ 2 ]{reset} {green}SETUP KickerFi{reset} {red}(NEED TO SET !){reset}")
print(" ")
print(f"{orange}[ 3 ]{reset} {orange}EXIT{reset}")

b = input("\nOption : ")
if b =="1":
    Start_KickerFi()
elif b =="2":
    SetupKickerFi()
elif b =="3":
    print("Exitting ...")
    exitting()
else:
    print("Invalid INPUT !")
    sleep(2)
    exitting()
