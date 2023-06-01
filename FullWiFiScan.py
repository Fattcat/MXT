import subprocess
import os

FileName = "Scan.txt"

os.system("clear")
Choice = input("Write wlan1 or wlan0 : ")
sub = subprocess.check_output(["sudo", "iw", "dev", Choice, "scan"])
sub = sub.decode("utf-8")
print("\nCHECK Your", FileName, "File (FOR ALL DETAILS)\n")
with open(FileName, "w") as file:
    file.write(sub)


#import subprocess
#print("Select WiFi Adapter wlan1 or wlan0")
#UserChoice = input("Write here  : ")
#sub = subprocess.check_output(["sudo","iw" ,"dev" ,UserChoice ,"scan"])
#sub = sub.decode("utf-8")
#print(sub)
#
#with open("scan.txt", "w")as file:
#    file.write(sub)