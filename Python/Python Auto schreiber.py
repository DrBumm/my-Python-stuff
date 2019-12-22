from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(10)

key_list = ["RXKFJ67HBV84TD2RMDK89BDMT", "3D2W38DJM6YKQRBB2XDBTVQHF"]
for key in key_list:
    time.sleep(5)
    for char in key:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)
        print(char)
    print(key)
