import os
import pickle
from typing import Any
import sys
import time
import random

import mouse

# Type Annotations
var1: str = 'mm_events.txt'
var2: str = 'mm_events1.txt'
var3: str = 'mm_events2.txt'
variables: list[str] = [var1, var2, var3]
max_time: float = time.time() + 1200


def disable_print() -> None:
    sys.stdout = open(os.devnull, 'w')


def enable_print() -> None:
    sys.stdout = sys.__stdout__


def run_mouse(mm_events, length) -> None:
    current_time: float = time.time()
    print("Hello!", flush=True)
    try:
        idx: int = 1
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


def load_events(event_file) -> Any:
    with open(f'{event_file}', 'rb') as file:
        return pickle.load(file)


def randomize_events() -> None:
    run_mouse(load_events(random.choice(variables)), random.randint(1, 5))


if __name__ == "__main__":
    if len(sys.argv) - 1 > 0:
        enable_print()
    else:
        disable_print()
    for i in range(random.randint(10, 20)):
        randomize_events()
