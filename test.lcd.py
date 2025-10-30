# test.lcd.py

from qliic_aleatoire import aleatoire

import qliic_i2clcd
import time

lcd = qliic_i2clcd.LCD(2, 16)

lcd.putstr("Allo, on Qliic  ensemble ?")
time.sleep(1)

try:
    while True:
        lcd.clear()
        lcd.move_to(aleatoire(12),aleatoire(1))
        lcd.putstr("Allo")
        time.sleep(1)

except KeyboardInterrupt:
        lcd.clear()
        lcd.putstr("Au revoir")
