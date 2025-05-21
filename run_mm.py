import os
import pickle
from typing import Any
import sys
import time
import random

import mouse

# Using Type Annotations
var1: str = 'events_0.dat'
var2: str = 'events_1.dat'
var3: str = 'events_2.dat'
var4: str = 'events_3.dat'
variables: list[str] = [var1, var2, var3, var4]
max_time: float = time.time() + 1200


def disable_print() -> None:
    sys.stdout = open(os.devnull, 'w')


def enable_print() -> None:
    sys.stdout = sys.__stdout__


def run_mouse(events, length) -> None:
    current_time: float = time.time()
    print("Hello!", flush=True)
    try:
        idx: int = 1
        for x in range(length):
            if current_time > max_time:
                exit()
            print(f"Working {idx}", flush=True)
            time.sleep(random.randint(5, 10))
            mouse.play(events[:-1])
            idx += 1
    except KeyboardInterrupt:
        print("Good Bye!")
        exit()


def load_events(event_file) -> Any:
    with open(f'{event_file}', 'rb') as file:
        return pickle.load(file)


def randomize_events() -> None:
    run_mouse(load_events(random.choice(variables)), random.randint(1, 3))


if __name__ == "__main__":
    disable_print()
    if len(sys.argv) - 1 > 0:
        # convert minutes to seconds
        max_time = time.time() + (int(sys.argv[1]) * 60)
    for i in range(random.randint(10, 20)):
        randomize_events()
