# Simple countdown timer

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\r', timer) # Pycharm issue? Not overwriting timer. Played round and line by line countdown only
        time.sleep(1)
        t -= 1
    print('Time to get back to work!')

t = int(input("How long before you get back to work?: "))

countdown(t)

