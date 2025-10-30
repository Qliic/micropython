# esp8266_pins.py

# Choisissez la broche GPIO à laquelle votre bouton est connecté.
# Par exemple:
# - Pour ESP32: GPIO 13, 27, 32, etc. (attention aux strapping pins comme GPIO0, GPIO2, GPIO12, GPIO15 sur certains ESP32)
# - Pour ESP8266: GPIO 0, 2, 4, 5, 12, 13, 14, 16 (attention à GPIO0 et GPIO2 pour le bootloader)


# D0	16	Ne supporte pas les interruptions, le PWM ou l'I2C. Peut être utilisée pour le "Deep Sleep".
# D1	5	Supporte le PWM, I2C (SCL).
# D2	4	Supporte le PWM, I2C (SDA).
# D3	0	Broche spéciale. Doit être HIGH au démarrage pour ne pas entrer en mode de flashage. Supporte le PWM.
# D4	2	Broche spéciale. Doit être HIGH au démarrage pour que la carte démarre correctement. Supporte le PWM.
# D5	14	Supporte le PWM, I2C, SPI.
# D6	12	Supporte le PWM, SPI.
# D7	13	Supporte le PWM, SPI.
# D8	15	Broche spéciale. Doit être LOW au démarrage pour que la carte démarre correctement. Supporte le PWM, SPI.
