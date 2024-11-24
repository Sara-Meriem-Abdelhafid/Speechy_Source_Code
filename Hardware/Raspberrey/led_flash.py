import gpiozero
import time
led = gpiozero.LED(17)


led1 = gpiozero.LED(27)
led2 = gpiozero.LED(22)
led3 = gpiozero.LED(23)
led4 = gpiozero.LED(24)


for i in range(10):
	led1.toggle()
	time.sleep(0.1)
	led1.toggle()
	time.sleep(0.2)
	led2.toggle()
	time.sleep(0.1)
	led2.toggle()
	time.sleep(0.2)
	led3.toggle()
	time.sleep(0.1)
	led3.toggle()
	time.sleep(0.2)
	led4.toggle()
	time.sleep(0.1)
	led4.toggle()
	time.sleep(0.2)






try:
    # Start the PWM with a 0-degree duty cycle (position the servo at 0 degrees)
    while True:
        servo = int(input())
        if(servo == 1):
            # Move the servo from 0 to 180 degrees
            led1.toggle()
            for angle in range(0, 181, 180):
            # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm1.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)
            led1.toggle()
            pwm1.ChangeDutyCycle(2.5)

        elif(servo == 2):
            # Move the servo from 0 to 180 degrees
            led2.toggle()
            for angle in range(0, 181, 180):
            # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm2.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)
            led2.toggle()
            pwm2.ChangeDutyCycle(2.5)

        elif(servo == 3):
            # Move the servo back from 180 to 0 degrees
            led3.toggle()
            for angle in range(180, -1, -180):
                # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm3.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)
            led3.toggle()
            pwm3.ChangeDutyCycle(2.5)

        elif(servo == 4):
            # Move the servo back from 180 to 0 degrees
            led4.toggle()
            for angle in range(180, -1, -180):
                # Map the angle to a duty cycle between 2.5% and 12.5%
                duty_cycle = 2.5 + (angle / 18)
                pwm4.ChangeDutyCycle(duty_cycle)
                time.sleep(0.5)
            led4.toggle()
            pwm4.ChangeDutyCycle(2.5)