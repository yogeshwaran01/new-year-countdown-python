import os
import time

from utils import count_down

while True:
    os.system('clear')
    print('{} Days {} Hours {} Minutes and {} Seconds'.format(*count_down()))
    time.sleep(1)
    os.system('clear')
