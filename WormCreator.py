from time import sleep
import os
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

os.system("clear")
sleep(1)

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
def RemoteAntivirusOff():
    pass

text = red + textos + reset
print(text)
sleep(2)
os.system("clear")
sleep(0.3)
print("\n")
print("\n")
print(f"[1] - Startuj nieco ...")
print(f"[2] - NASTAV nieco ...")
print(f"[3] - ULOZ nieco ...")
print(f"[4] - SPUSTI na inom PC nieco ...")
print(f"[5] - Startuj nieco ...")
print(f"[6] - Startuj nieco ...")
print(f"[7] - Startuj nieco ...")
print(f"[8] - Startuj nieco ...")
print(f"[9] - NASTAVENIA ...")
print(f"[10] - EXIT")
print("\n")
print("\n")
Option = input("Select : ")