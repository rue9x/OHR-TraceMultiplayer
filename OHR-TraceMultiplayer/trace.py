import os
import sys
import time

SAVE_FOLDER = os.path.dirname(os.path.realpath(__file__))

filePath = os.path.join(SAVE_FOLDER,"g_debug.txt")


lastLine = None

while True:
    with open(filePath,'r') as f:
        lines = f.readlines()
    if lines[-1] != lastLine:
        lastLine = lines[-1]
        print(lines[-1])
    time.sleep(1)