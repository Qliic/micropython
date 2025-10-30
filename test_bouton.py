# test_bouton.py

from time import *
import machine


from qliic_bouton import BOUTON # Importer la classe ClicBouton

BOUTON_D7 = 13 # D7

last_state = False # Pour détecter les changements d'état

pin_d7 = machine.Pin(BOUTON_D7, machine.Pin.IN, machine.Pin.PULL_UP)

# --- Code principal ---
if __name__ == '__main__':
    #NeoPixelController.test()
    
    while True:
        #bouton_loop(bouton_d7)
        print(pin_d7.value())
        sleep_ms(100)
    
    
    

