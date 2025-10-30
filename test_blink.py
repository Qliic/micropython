# test_blink.py

from machine import Pin
import time

# Initialisez la LED. La broche (Pin) varie selon la carte.
# Par exemple, 'LED' ou un numéro de broche comme 2 (pour certaines cartes ESP32/ESP8266),
# L'exemple ci-dessous utilise le Pin(2) comme point de départ.

led = Pin(2, Pin.OUT)

# Boucle infinie pour faire clignoter la LED
while True:
    led.value(1)    # Allumer la LED (ou led.on())
    time.sleep(0.5) # Attendre 0.5 seconde
    led.value(0)    # Éteindre la LED (ou led.off())
    time.sleep(0.5) # Attendre 0.5 seconde
