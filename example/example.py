import time

from simple_interval import set_interval, clear_interval


def print_hello():
    print("Hello, world!")


interval = set_interval(print_hello, 1.0)

try:
    while True:
        # Do other stuff...
        print("  Doing other stuff...")
        time.sleep(0.25)
except KeyboardInterrupt:
    # Stop the interval
    clear_interval(interval)
