# test_pot.py

from machine import ADC
from time import sleep

# Initialiser l'objet ADC sur le pin A0 (canal 0 pour l'ESP8266)
pot = ADC(0) 

while True:
    # Lire la valeur analogique (généralement entre 0 et 1023 pour l'ESP8266)
    valeur_pot = pot.read() 
    
    # Afficher la valeur
    print("Valeur du potentiomètre :", valeur_pot) 
    
    # Attendre un peu avant la prochaine lecture
    sleep(0.1)
