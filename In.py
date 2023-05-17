import os

from time import sleep

import subprocess

def install(package):

    try:

        subprocess.check_call(["pip3", "install", package])

    except subprocess.CalledProcessError as e:

        print(f"Chyba pri inštalácii balíka {package}: {e}")

        install(package)  # Opakovane sa pokús o inštaláciu

def apt_install(package):

    try:

        subprocess.check_call(["sudo", "apt-get", "install", package])

    except subprocess.CalledProcessError as e:

        print(f"Chyba pri inštalácii balíka {package}: {e}")

        apt_install(package)  # Opakovane sa pokús o inštaláciu

try:

    install("playsound")

    sleep(1)

    install("pyautogui")

    sleep(1)

    install("pywifi")

    sleep(1)

    install("pygame")

    sleep(1)

    install("shutil")

    sleep(1)

    apt_install("wireless-tools")

except Exception as e:

    print(f"Vyskytla sa chyba: {e}")

