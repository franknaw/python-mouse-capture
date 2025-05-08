import os
import pickle
import sys
import time
import random

import mouse

var1 = 'mm_events.txt'
var2 = 'mm_events1.txt'
var3 = 'mm_events2.txt'
variables = [var1, var2, var3]
max_time = time.time() + 600


def disable_print():
    sys.stdout = open(os.devnull, 'w')


def enable_print():
    sys.stdout = sys.__stdout__


def run_mouse(mm_events, length):
    current_time = time.time()
    print("Hello!", flush=True)
    try:
        idx = 1
        for x in range(length):
            if current_time > max_time:
                exit()
            print(f"Working {idx}", flush=True)
            time.sleep(random.randint(5, 10))
            mouse.play(mm_events[:-1])
            idx += 1
    except KeyboardInterrupt:
        print("Good Bye!")
        exit()


def load_events(event_file):
    f = open(f'{event_file}', 'rb')
    event = pickle.load(f)
    f.close()
    return event


def randomize_events():
    run_mouse(load_events(random.choice(variables)), random.randint(1, 5))


if __name__ == "__main__":
    if len(sys.argv) - 1 > 0:
        enable_print()
    else:
        disable_print()
    for i in range(random.randint(10, 20)):
        randomize_events()
