# sors_de_ma_chambre.py

from time import *

from qliic_aleatoire import aleatoire

# lcd sur D1, D2
import qliic_i2clcd
lcd = qliic_i2clcd.LCD(2, 16)

# potentiometre sur A0
from machine import ADC
pot = ADC(0)

# bouton sur D6=12
BOUTON_PIN = 12 
pin_d7 = machine.Pin(BOUTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

# hcsr04
from qliic_hcsr04 import HCSR04
# D7 D8
sensor = HCSR04(trigger_pin=13, echo_pin=15)

# RGB
from qliic_neopixel import NEOPIXEL
# D3=0
my_neopixel = NEOPIXEL(0, 5)
my_neopixel.clear()

# servo D5

#from qliic_servo import *

# init

my_neopixel.set_pixel_color(0, 128, 0, 0)
my_neopixel.show()
sleep(1)
my_neopixel.set_pixel_color(0, 0, 128, 0)
my_neopixel.show()
sleep(1)
my_neopixel.set_pixel_color(0, 0, 0, 128)
my_neopixel.show()
sleep(1)

lcd.putstr("Allo, on Qliic  ensemble ?")
sleep(1)
lcd.clear()

try:
    while True:
        pot_valeur = pot.read()
        bouton = pin_d7.value()
        distance = int(sensor.distance_cm())
        
        pot_str = f"{pot_valeur}    "
        lcd.move_to(0, 0)
        lcd.putstr(f"pot: {pot_str}")
        lcd.move_to(0, 1)
        lcd.putstr(f"bout: {bouton} cm: {distance}  ")
        
        if (bouton == 0):   
            #my_neopixel.set_pixel_color(0, int(pot_valeur/4), 0, 0)
            my_neopixel.set_pixel_color(0, int(distance), 0, 0)
            my_neopixel.show()
        else:
            my_neopixel.set_pixel_color(0, 0, 0, 0)
            my_neopixel.show()
        
        #set_servo_angle(servo_pwm, pot_valeur)
        
        sleep_ms(100)

except KeyboardInterrupt:
        lcd.clear()
        lcd.putstr("Au revoir")
