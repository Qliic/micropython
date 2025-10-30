# qliic_servo.py

from machine import Pin, PWM
import time

# --- Configuration des constantes ---
# Broche GPIO à laquelle le fil de signal du servo est connecté
SERVO_PIN = 14 # D5 
# Fréquence standard du servomoteur (50 Hz = période de 20 ms)
SERVO_FREQ = 50

# Plages de Duty Cycle pour un servo 0-180 degrés (ajustez si nécessaire)
# Ces valeurs sont pour une résolution 16-bit (0-65535) comme sur la Pi Pico.
# 0 degré correspond à environ 1 ms d'impulsion.
# 180 degrés correspond à environ 2 ms d'impulsion.
DUTY_MIN = 1500  # Duty pour 0 degré (environ 0.5 ms/20 ms * 65535)
DUTY_MAX = 8500  # Duty pour 180 degrés (environ 2.5 ms/20 ms * 65535)
# Note: Ces valeurs peuvent varier, ajustez pour que le servo n'aille pas au-delà de ses limites.


def set_servo_angle(pwm_object, angle):
    """
    Convertit un angle (0-180) en Duty Cycle et déplace le servo.
    """
    # Conversion de la plage d'angle (0-180) à la plage de Duty Cycle (DUTY_MIN à DUTY_MAX)
    # Formule de mapping : y = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    # Assurer que l'angle est entre 0 et 180
    angle = max(0, min(180, angle))
    
    # Calcul du Duty Cycle
    duty = int((angle / 180) * (DUTY_MAX - DUTY_MIN) + DUTY_MIN)
    
    # Appliquer le Duty Cycle
    pwm_object.duty_u16(duty)


# --- Initialisation ---
servo_pwm = PWM(Pin(SERVO_PIN))
servo_pwm.freq(SERVO_FREQ)

def test_servo():
    print("Démarrage du balayage du servomoteur...")

    # --- Boucle Principale (Balayage) ---
    while True:
        # 1. Balayage de 0 à 180 degrés
        for angle in range(0, 181, 5): # De 0 à 180, par pas de 5 degrés
            set_servo_angle(servo_pwm, angle)
            time.sleep(0.05) # Petite pause pour le mouvement

        time.sleep(0.5) # Pause à 180 degrés

        # 2. Balayage de 180 à 0 degrés
        for angle in range(180, -1, -5): # De 180 à 0, par pas de -5 degrés
            set_servo_angle(servo_pwm, angle)
            time.sleep(0.05) # Petite pause pour le mouvement

        time.sleep(0.5) # Pause à 0 degré

