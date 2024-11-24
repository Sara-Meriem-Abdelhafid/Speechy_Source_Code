from gpiozero import DistanceSensor
from time import sleep

# Define the GPIO pins for the ultrasonic sensor
trigger_pin = 26
echo_pin = 20

# Create an ultrasonic sensor object
ultrasonic_sensor = DistanceSensor(echo=echo_pin, trigger=trigger_pin)

try:
    while True:
        distance = ultrasonic_sensor.distance
        print(f"Distance: {distance:.2f} meters")
        sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by the user")
finally:
    print("Cleanup GPIO")
