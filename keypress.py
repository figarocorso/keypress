#!/usr/bin/env python
# Play sounds on keypresses in Linux
# Originally by Sayan "Riju" Chakrabarti (sayanriju)
# http://rants.sayanriju.co.cc/script-to-make-tick-tick-sound-on-keypres

from Xlib.display import Display
import threading
import os
import time

ZERO, SHIFT, ALT, CTL = [], [], [], []
for i in range(0, 32):
    ZERO.append(0)
    if i == 6:
        SHIFT.append(4)
    else:
        SHIFT.append(0)
    if i == 4:
        CTL.append(32)
    else:
        CTL.append(0)
    if i == 8:
        ALT.append(1)
    else:
        ALT.append(0)

ignorelist = [ZERO,  ALT,  SHIFT,  CTL]


class KeyPress(threading.Thread):
    def run(self):
        os.system("aplay sounds/key01.wav")


def main():
    disp = Display()
    while 1:
        keymap = disp.query_keymap()
        if keymap not in ignorelist:
            KeyPress().start()
            time.sleep(0.08)


if __name__ == '__main__':
    main()
