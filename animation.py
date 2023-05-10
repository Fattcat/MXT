from time import sleep
import os

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'

#orange = '\033[033m'
orange = '\033[38;5;208m'

magenta = '\033[35m'
cyan = '\033[36m'
reset = '\033[0m'

while True:
    #os.system("clear")
    sleep(1)
    print("")
    print("")
    print(f"{green}+---+{reset}       ")
    print(f"{green}| O |{reset}       ")
    print(f"{green}+---+{reset}        (\ ")
    print("         )O   (\ ")
    print("      --->)    (|")
    print("         )O    )")
    print("              (/")
    print("+---+        (/")
    print("| O |        ")
    print("+---+        ")
    print("")
    print("")
    
    sleep(1)

    os.system("clear")

    sleep(1)
    print("")
    print("")
    print(f"  {red}(+---+){reset}      ")
    print(f"  {red}(| | |){reset}      ")
    print(f"  {red}(+---+){reset}     (\ ")
    print("            )O (\ ")
    print("         --->)   (|")
    print("            )O   )")
    print("                (/")
    print("   +---+        (/")
    print("   | O |        ")
    print("   +---+        ")
    print("")
    print("")

