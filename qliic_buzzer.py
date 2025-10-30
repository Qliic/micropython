# qliic_buzzer.py 

from machine import Pin, PWM
import time

class BUZZER:
    """
    Classe pour contrôler un buzzer passif via PWM (Pulse Width Modulation)
    sur un microcontrôleur MicroPython (comme ESP32/ESP8266).
    """
    
    # Fréquences des notes (La4 = 440 Hz) pour une octave
    # Note: L'index 0 est la note 'La'
    # Utilisation d'un dictionnaire pour plus de clarté
    FREQUENCIES = {
        'C': 261.63, 'C#': 277.18, 'Db': 277.18,
        'D': 293.66, 'D#': 311.13, 'Eb': 311.13,
        'E': 329.63,
        'F': 349.23, 'F#': 369.99, 'Gb': 369.99,
        'G': 392.00, 'G#': 415.30, 'Ab': 415.30,
        'A': 440.00, 'A#': 466.16, 'Bb': 466.16,
        'B': 493.88
    }

    def __init__(self, pin_number, duty_cycle=512):
        print("init", pin_number, duty_cycle)
        """
        Initialise le buzzer PWM.
        
        :param pin_number: Le numéro de la broche GPIO connectée au buzzer.
        :param duty_cycle: Le cycle de travail (0-1023) pour une onde carrée (par défaut 512 = 50%).
        """
        self.pin_number = pin_number
        self.duty_cycle = duty_cycle
        # Initialisation du PWM, fréquence initiale à 0 pour être silencieux
        self.pwm = PWM(Pin(pin_number), freq=0, duty=0)

    def tone(self, frequency, duration_ms):
        """
        Joue une fréquence pendant une durée spécifiée.
        
        :param frequency: La fréquence en Hz (ex: 440 pour La).
        :param duration_ms: La durée en millisecondes.
        """
        if frequency > 0:
            print("tone", frequency, duration_ms, self.duty_cycle)
            self.pwm.freq(frequency)
            self.pwm.duty(self.duty_cycle)  # Active le buzzer
            time.sleep_ms(duration_ms)
        else:
             # Si la fréquence est 0, c'est un silence (pause)
             self.pwm.duty(0)

        self.pwm.duty(0)  # Éteint le buzzer après la durée
        # Ajouter une courte pause pour éviter que les notes ne se chevauchent
        time.sleep_ms(20) 

    def play_note(self, note, duration_ms, octave=4):
        #print(note, duration_ms, octave)
        
        """
        Joue une note à partir de la table de fréquences.
        
        :param note: Nom de la note (ex: 'A', 'C#', 'Eb').
        :param duration_ms: La durée en millisecondes.
        :param octave: L'octave (par défaut 4). Chaque octave augmente la fréquence par 2.
        """
        if note == 'R' or note == 'r': # 'R' pour Reste (silence)
            self.tone(0, duration_ms)
            return

        note_upper = note.upper()
        if note_upper in self.FREQUENCIES:
            base_freq = self.FREQUENCIES[note_upper]
            # Calcul de la fréquence pour l'octave spécifiée
            frequency = base_freq * (2**(octave - 4))
            self.tone(int(frequency), duration_ms)
        else:
            print(f"Note '{note}' non reconnue.")
            
    def deinit(self):
        """Désactive le PWM, met la broche à zéro, et libère la ressource."""
        self.pwm.duty(0)
        self.pwm.deinit()
        # Optionnel: Réinitialiser la Pin en mode sortie ou entrée pour s'assurer qu'elle est "propre"
        # Pin(self.pin_number, Pin.IN)
        time.sleep_ms(50) # courte attente pour que le hardware se réinitialise

    def __exit__(self, exc_type, exc_value, traceback):
        """Méthode appelée à la fin du bloc 'with' (pour nettoyer)."""
        self.deinit()
        # Renvoyer False pour propager les exceptions, ou True pour les supprimer
        return False
    
def test_buzzer():
    # Initialisation du buzzer sur la broche 14 (adapté pour ESP8266 NodeMCU)
    # Assurez-vous d'adapter le numéro de broche à votre montage (par exemple, 4 sur certains ESP32)
    BUZZER_PIN = 14 
    
    try:
        mon_buzzer = BUZZER(BUZZER_PIN)
        
        # Définir une durée de base (par exemple, des croches)
        duree_note = 250 
        
        mon_buzzer.play_note('C', duree_note, octave=5)
        mon_buzzer.play_note('E', duree_note, octave=5)
        mon_buzzer.play_note('G', duree_note, octave=5)
        mon_buzzer.play_note('C', duree_note, octave=5)
        mon_buzzer.play_note('R', duree_note) # Silence
        
    except Exception as e:
        print(f"Erreur lors de l'exécution: {e}")
        
    finally:
        # Nettoyage
        if 'mon_buzzer' in locals():
            mon_buzzer.deinit()
            print("Buzzer désactivé.")

def test():
    # Initialisation du buzzer sur la broche 14 (adapté pour ESP8266 NodeMCU)
    # Assurez-vous d'adapter le numéro de broche à votre montage (par exemple, 4 sur certains ESP32)
    BUZZER_PIN = 12 # D6
    
    mon_buzzer = BUZZER(BUZZER_PIN)
    print("Buzzer activé.")
    
    # Définir une durée de base (par exemple, des croches)
    duree_note = 250 
    
    #mon_buzzer.play_note('C', duree_note, octave=5)
    #mon_buzzer.play_note('E', duree_note, octave=5)
    #mon_buzzer.play_note('G', duree_note, octave=5)
    mon_buzzer.play_note('C', duree_note, octave=4)
    mon_buzzer.play_note('C', duree_note, octave=5)
    mon_buzzer.play_note('C', duree_note, octave=6)
    mon_buzzer.play_note('R', duree_note) # Silence
    
    mon_buzzer.deinit()


test()
