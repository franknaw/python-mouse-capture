import mouse
import pickle


def capture_events(file_i) -> None:
    events: list = mouse.record()
    with open(f'events_{file_i}.dat', 'wb') as file:
        pickle.dump(events, file)


if __name__ == "__main__":
    for i in range(4):
        capture_events(i)
