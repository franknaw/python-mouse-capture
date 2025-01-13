import mouse
import time
import pickle


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
    run_mouse(load_events(), 100)

