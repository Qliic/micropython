# test.hcsr04.py

# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/

from qliic_hcsr04 import HCSR04
import time

# D7 D8
sensor = HCSR04(trigger_pin=13, echo_pin=15)
# D3 D4
#sensor = HCSR04(trigger_pin=0, echo_pin=2)
# D1 D2
#sensor = HCSR04(trigger_pin=4, echo_pin=5)

# ESP8266
#sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

while True:
    distance = sensor.distance_cm()
    print('cm:', distance)
    time.sleep_ms(100)
