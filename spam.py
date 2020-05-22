import json
import logging
import os
import time


logging.basicConfig(format="%(asctime)s %(message)s")


def main():
    my_guid = os.getenv("CF_INSTANCE_GUID", "¯\_(ツ)_/¯")
    counter = 0
    while True:
        logging.warning(f"{my_guid} - {counter}")
        counter += 1
        time.sleep(0.5)


if __name__ == "__main__":
    main()
