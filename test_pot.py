# test_pot.py

from machine import Pin, ADC
import time

# ESP32

adc_1 = ADC(Pin(15))
adc_2 = ADC(Pin(4))

print("Démarrage de la lecture du potentiomètre...")

# 3. Boucle de lecture
while True:
    # Lire la valeur analogique (un nombre entier entre 0 et 4095)
    raw_value_1 = adc_1.read()
    raw_value_2 = adc_2.read()
    
    print(f"P1: {raw_value_1: <4} P2: {raw_value_2: <4}")
    
    time.sleep(0.1) # Lire toutes les 100 millisecondes
