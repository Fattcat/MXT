from time import sleep
import os
import keyboard
import subprocess
import random
import socket

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

def BYEBYE():
        print("")
        print("")
        print(f"        {blue}+--------------------------------------------+{reset}")
        print(f"              |            {yellow}BYE BYE              {reset}|")
        print(f"              |  {green}Thank You for using stt.py{reset}     |")
        print(f"        {blue}+--------------------------------------------+{reset}")
        print("")
        print("")
        sleep(1)
        os.system("clear")

os.system("clear")
sleep(1)
print(f"                 Welcome to {red}WormCreator.py{reset}")
print(f"\n                   Created by {orange}Fattcat{reset}\n     GitHub Link : {green}https://github.com/Fattcat/MXT/{reset}")
textos = """
    

                    .:^^^~^^~~~~^^~^^^:.                    
                .:~!~^::.~~^:..:^~^.::^~!~:.                
              :~!JY^      ^!^~~^!^      ^YJ!~:              
            ~!^. !!~!!!!?~J.    .J~?!!!!^!! .^!~            
          ^J?.7!~~^..~^.?~?     .?~?.~~..^~~!7.?J^          
        .?~.~:~~:::^~!!77!7~    !7!77!!~^:::~~:~.!?.        
       .J?~:7~!?7:^~:~7?^!^7~^^~7^!^?!~.~^:7?~~7:!?J.       
       ?^.J ^7.7.?7J~~~!~!? !77! ?!~!~~~J7?.7.7: J.^?       
      ^Y^?:.~!.!^..J!7 :~^7^.~~.^7^~: 7!J..^!.!~.:?^Y^      
      7! :7!:^^~^: :~:   ~7::~~:^7~   :~: :^~~^:!?: 77      
      77:~:^^^^~!7!7~7!7^!~J:..:J~!^7!!~7!7!~^^^^:~:?7      
      !?!:7^.~?!~:.   .^!?^^^..^^^?!:.   .:~!?~.~7:!J!      
      ^Y~!?.7Y:          !J^ ~^ ^J~          ^Y!:?!~Y^      
       5??7?J?           :5! ^^ !5.           ?J?7??5       
       7J!!J!J^         .7J:....:J7.         ^J!J!~J7       
       !5~~:^~J?~^^:^~!7?7^.^77^.^??7!^^:^^~?J~^:~~5!       
      ?~.~~~! .~!7?77!~^.: ~!.:!~ :.^!!77?7!~. !^~~.!7      
     .Y.7!^J:^!7~:..    ..!~    ~!..    ..:~7!^:J^!7.Y.     
      !7^7^!^!7J?777?~  .^? .^^. J^.  ~?777?J7!^!^7^7!      
       :~^^^?Y??7~.^P? ^  ^!~~~~!^  : JP^.~7??Y7^^^~:       
             !!:~? ~7.!:^ ^  ^^  ^ ^:!.7~ ?~:7!             
              J:!? 7!J?!J~?7~77~7?!J!JJ77.?!:J              
              J!~?:~!!!^!::~ ?7 ~::!~!!!^:?~!J              
             .J^~7?77!7^7.!^.?7.^~:7^7!?7?7~^J.             
             :?^!~!!?7~7^7^!.J?.!^7^7~7?!!~!^?.             
              ?7!~^~7!?777!?~J?~?!777?!7~^~!7?              
              .?7!!!.~^.7!   ::   !7.~~.!!77?.              
                ~7!7:^^ ~!^:^^^^:^!~ ^::7!7~                
                  :~?J~^^!?^....^?!^^~J7~:                  
                     ^~^~~!~~77~~!~~^~^                     
                       .~!!7!::!7!!~. 
                       
                                                            """
sleep(2)

def handle_ctrl_c(signal, frame):
    print("Dovidenia :D")
    signal.signal(signal.SIGINT, handle_ctrl_c)
    exit(0)

def RemoteAntivirusOff():
    pass

text = red + textos + reset
print(text)
sleep(2)
os.system("clear")
sleep(0.3)
print("\n")
print("\n")
print(f"   {green}Your Main Menu{reset}\n")
print(f"[ {yellow}1{reset} ] - Startuj nieco ...")
print(f"[ {yellow}2{reset} ] - NASTAV nieco ...")
print(f"[ {yellow}3{reset} ] - ULOZ nieco ...")
print(f"[ {yellow}4{reset} ] - SPUSTI na inom PC nieco ...")
print(f"[ {yellow}5{reset} ] - Startuj nieco ...")
print(f"[ {yellow}6{reset} ] - Startuj nieco ...")
print(f"[ {yellow}7{reset} ] - Startuj nieco ...")
print(f"[ {yellow}8{reset} ] - Startuj nieco ...")
print(f"[ {yellow}9{reset} ] - NASTAVENIA ...")
print(f"[ {red}10{reset} ] - EXIT")
print("\n")
print("\n")
Option = input("Select : ")
if Option == "1":
    pass

elif Option == "2":
    os.system("python3 WormSetupper.py")

elif Option == "3":
    pass

elif Option == "4":
    pass

elif Option == "5":
    pass

elif Option == "6":
    pass

elif Option == "7":
    pass

elif Option == "8":
    pass

elif Option == "9":
    pass

elif Option == "10":
    BYEBYE()
    sleep(1)
    exit()

else:
    print(f"{red}Invalid INPUT !{reset}")

while True:
    if keyboard.is_pressed('ctrl+c'):
      handle_ctrl_c()
      keyboard.wait('esc')
      print("           ------------")
      print("Exitting ( < O > : < O > )")
      print("           ------------")
      sleep(1)
      exit()
