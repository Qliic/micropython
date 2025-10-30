# qliic_aleatoire.py

import time

# --- 1. Obtenir une "graine" (seed) imprévisible ---
# La fonction time.ticks_us() retourne le nombre de microsecondes écoulées
# depuis le démarrage de la carte, ce qui est une excellente source
# de variabilité pour un générateur de nombres.

# --- 2. Fonction de génération simplifiée (LFSR de base) ---
# On utilise une opération arithmétique simple pour transformer la graine
# en un nouveau nombre "aléatoire" à chaque appel.
def aleatoire(max_valeur):
    # Algorithme de mélange simple (peut être un LFSR, une congruence linéaire, etc.)
    # Multiplier par un grand nombre premier, ajouter un autre, et prendre le reste (modulo).
    graine = (time.ticks_us() * 1103515245 + 12345) & 0xFFFFFFFF
    
    # Ramener le résultat dans la plage [0, max_valeur - 1]
    nombre_aleatoire = (graine % (max_valeur + 1))
    
    return nombre_aleatoire

def test():
    # Générer et afficher 5 nombres
    for i in range(100):
        resultat = aleatoire(10) # Génère entre 0 et 100
        print(f"Tentative {i}: {resultat}")

#test()
