import mouse
import pickle


def capture_mm() -> None:
    mm_events: list = mouse.record()
    with open('mm_events.txt', 'wb') as file:
        pickle.dump(mm_events, file)


if __name__ == "__main__":
    capture_mm()
