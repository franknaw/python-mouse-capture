import mouse
import pickle


def capture_mm():
    mm_events = mouse.record()
    f = open('mm_events.txt', 'wb')
    pickle.dump(mm_events, f)
    f.close()


if __name__ == "__main__":
    capture_mm()

