import RPi.GPIO as GPIO
RED_PIN = 11
GREEN_PIN = 13
BLUE_PIN = 15

current_pin = BLUE_PIN
GPIO.setmode(GPIO.BOARD)
GPIO.setup(current_pin, GPIO.OUT)

p = GPIO.PWM(current_pin, 100)
p.start(1)
raw_input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()