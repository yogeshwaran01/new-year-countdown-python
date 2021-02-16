import os
import time

from utils import count_down, india_zone

while True:
    os.system("clear")
    print("{day} Days {hour} Hours {min} Minutes and {sec} Seconds".format(**count_down(india_zone)))
    time.sleep(1)
    os.system("clear")
