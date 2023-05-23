import os
from time import sleep
import time
os.system("clear")
sleep(0.2)
def animate_loading():
    bar_length = 20
    total_iterations = 50
    sleep_time = 0.1
    for i in range(total_iterations + 1):
        percent = i * 100 / total_iterations
        filled_length = int(bar_length * i / total_iterations)
        bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length)
        print(f'\r[{bar}] {percent:.0f}%', end='', flush=True)
        time.sleep(sleep_time)
    print("\nDownload sucessfully completed ! ")
animate_loading()
