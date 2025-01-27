import os
import pickle
import sys
import time

import mouse


def disable_print():
    sys.stdout = open(os.devnull, 'w')


def enable_print():
    sys.stdout = sys.__stdout__


def run_mouse(mm_events, length):
    print("Hello!", flush=True)
    try:
        idx = 1
        for x in range(length):
            print(f"Working {idx}", flush=True)
            time.sleep(30)
            mouse.play(mm_events[:-1])
            idx += 1
    except KeyboardInterrupt:
        print("Good Bye!")
        exit()


def load_events():
    f = open('mm_events.txt', 'rb')
    event = pickle.load(f)
    f.close()
    return event


if __name__ == "__main__":
    if len(sys.argv) - 1 > 0:
        if sys.argv[1] == "show":
            enable_print()
    else:
        disable_print()
    run_mouse(load_events(), 100)
