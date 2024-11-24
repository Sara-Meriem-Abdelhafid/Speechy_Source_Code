import  time

pwm_frequency = 50

pin1=5
pin2=6
pin3=12
pin4=13

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

pwm1=GPIO.PWM(pin1, pwm_frequency)
pwm2=GPIO.PWM(pin2, pwm_frequency)
pwm3=GPIO.PWM(pin3, pwm_frequency)
pwm4=GPIO.PWM(pin4, pwm_frequency)

pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)
print ("which servo 1,2,3 4 ??")

try:
    while True:
        servo = int(input())
        if(servo ==1 ):
            # Move the servo from 0 to 180 degrees
            for angle in range(0, 181, 180):                        # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle =2.5 + (angle / 18)
                pwm1.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)

            # Move the servo back from 180 to 0 degrees
            for angle in range(180, -1, -180):
                # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle =2.5 + (angle / 18)
                pwm1.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)
#pwm1.start(0)
#pwm2.start(0)
#pwm3.start(0)
#pwm4.start(0)

except KeyboardInterrupt:
    # Clean up GPIO on program exit
    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    pwm4.stop()

    GPIO.cleanup()

        if(servo == 2):
            # Move the servo from 0 to 180 degrees
            for angle in range(0, 181, 180):
            # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm2.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)

            # Move the servo back from 180 to 0 degrees
            for angle in range(180, -1, -180):
                # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm2.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)

        if(servo == 3):
            # Move the servo from 0 to 180 degrees
            for angle in range(0, 181, 180):
            # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm3.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)

            # Move the servo back from 180 to 0 degrees
            for angle in range(180, -1, -180):
                # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm3.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)
        
        if(servo == 4):
            # Move the servo from 0 to 180 degrees
            for angle in range(0, 181, 180):
            # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm4.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)

            # Move the servo back from 180 to 0 degrees
            for angle in range(180, -1, -180):
                # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm4.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)
            # Move the servo from 0 to 180 degrees
            for angle in range(0, 181, 180):
            # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm4.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)

            # Move the servo back from 180 to 0 degrees
            for angle in range(180, -1, -180):



                # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)




try:
    # Start the PWM with a 0-degree duty cycle (position the servo at 0 degrees)
    while True:
        servo = int(input())
        if(servo == 1):
            # Move the servo from 0 to 180 degrees
            for angle in range(0, 181, 180):
            # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm1.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)

            # Move the servo back from 180 to 0 degrees
            for angle in range(180, -1, -180):
                # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm1.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)
            pwm1.stop()

        elif(servo == 2):
            # Move the servo from 0 to 180 degrees
            for angle in range(0, 181, 180):
            # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm2.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)







try:
    # Start the PWM with a 0-degree duty cycle (position the servo at 0 degrees)
    while True:
        servo = int(input())
        if(servo == 1):
            # Move the servo from 0 to 180 degrees
            for angle in range(0, 181, 180):
            # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm1.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)

            # Move the servo back from 180 to 0 degrees
            for angle in range(180, -1, -180):
                # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm1.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)              
            pwm1.stop()

        elif(servo == 2):
            # Move the servo from 0 to 180 degrees
            for angle in range(0, 181, 180):
            # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm2.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)

            # Move the servo back from 180 to 0 degrees
            for angle in range(180, -1, -180):
                # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm2.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)
            pwm2.stop()

        elif(servo == 3):
            # Move the servo from 0 to 180 degrees
            for angle in range(0, 181, 180):
            # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm3.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)

            # Move the servo back from 180 to 0 degrees
            for angle in range(180, -1, -180):
                # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm3.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)
            pwm1.stop()

        elif(servo == 4):
            # Move the servo from 0 to 180 degrees
            for angle in range(0, 181, 180):
            # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm4.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)

            # Move the servo back from 180 to 0 degrees
            for angle in range(180, -1, -180):
                # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm4.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)
            pwm4.stop()
                          
except KeyboardInterrupt:
    GPIO.cleanup()