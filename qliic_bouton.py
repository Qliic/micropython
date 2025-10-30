# qliic_bouton.py
# Ce fichier contient la classe ClicBouton pour MicroPython

import machine
import time

class BOUTON:
    """
    Classe pour gérer un bouton physique connecté à une broche GPIO.
    Gère l'initialisation de la broche en entrée avec un pull-up ou pull-down interne.
    """

    def __init__(self, pin_number, pull_up=True):
        """
        Initialise le bouton sur une broche GPIO spécifique.
        :param pin_number: Le numéro de la broche GPIO à laquelle le bouton est connecté.
        :param pull_up: Si True (par défaut), active la résistance de pull-up interne.
                        Cela signifie que la broche sera HIGH (1) quand le bouton n'est PAS pressé,
                        et LOW (0) quand il est pressé (bouton connecté à GND).
                        Si False, active la résistance de pull-down interne.
                        La broche sera LOW (0) quand le bouton n'est PAS pressé,
                        et HIGH (1) quand il est pressé (bouton connecté à VCC).
        """
        self.pin_number = pin_number
        
        # Définir le type de pull (résistance interne)
        if pull_up:
            self.pin = machine.Pin(pin_number, machine.Pin.IN, machine.Pin.PULL_UP)
            self.pressed_state = 0 # Le bouton est pressé quand la pin est LOW
            print(f"Bouton initialisé sur GPIO {pin_number} avec PULL_UP. Pressé si LOW.")
        else:
            self.pin = machine.Pin(pin_number, machine.Pin.IN, machine.Pin.PULL_DOWN)
            self.pressed_state = 1 # Le bouton est pressé quand la pin est HIGH
            print(f"Bouton initialisé sur GPIO {pin_number} avec PULL_DOWN. Pressé si HIGH.")

    def est_presse(self):
        """
        Retourne True si le bouton est pressé, False sinon.
        """
        return self.pin.value() == self.pressed_state

    def attendre_pression(self, timeout_ms=0):
        """
        Attend que le bouton soit pressé.
        :param timeout_ms: Durée maximale en millisecondes à attendre. Si 0 (par défaut), attend indéfiniment.
        :return: True si le bouton a été pressé avant le timeout, False sinon.
        """
        start_time = time.ticks_ms()
        while not self.est_presse():
            if timeout_ms > 0 and time.ticks_diff(time.ticks_ms(), start_time) > timeout_ms:
                return False
            time.sleep_ms(10) # Petite pause pour ne pas surcharger le CPU
        return True

    def attendre_relachement(self, timeout_ms=0):
        """
        Attend que le bouton soit relâché.
        :param timeout_ms: Durée maximale en millisecondes à attendre. Si 0 (par défaut), attend indéfiniment.
        :return: True si le bouton a été relâché avant le timeout, False sinon.
        """
        start_time = time.ticks_ms()
        while self.est_presse():
            if timeout_ms > 0 and time.ticks_diff(time.ticks_ms(), start_time) > timeout_ms:
                return False
            time.sleep_ms(10) # Petite pause pour ne pas surcharger le CPU
        return True

    def deinit(self):
        """
        Désinitialise la broche du bouton.
        """
        # La méthode deinit() n'existe pas directement sur machine.Pin pour libérer
        # les pull-ups/downs ou les fonctions. Il faut généralement juste laisser l'objet
        # être collecté par le garbage collector, ou le réinitialiser si besoin.
        # Pour une réinitialisation explicite de la broche:
        self.pin = None # Retire la référence à l'objet Pin
        print(f"Bouton sur GPIO {self.pin_number} désinitialisé (référence supprimée).")

