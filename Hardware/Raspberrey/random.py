#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO
import os

#from random import randint
import random

GPIO.setmode(GPIO.BCM)

# Definieer de pinnen van de ULN2003A in relatie tot de GPIO
IN1=6 # IN1
IN2=13 # IN2
IN3=19 # IN3
IN4=26 # IN4

# Wachttijd regelt de draaisnelheid van de motor
time = 0.001

# GPIO pinnen uitgangen definieren
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

# Alle pinnen worden op False gezet. De reden dat de motor niet direct draait
GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

# De stappenmotor 28BYJ-48 is zo gebouwd, dat de motor intern
# 8 stappen voor een omdraaiing nodig heeft. Door de tandwielen
# heeft het 512 x 8 stappen nodig om de as 360 te laten draaien.

# Definitie van stappen 1 - 8 over pinnen IN1 toto IN4:
# Tussen elke beweging van de motor wordt even gewacht
# om de motoranker zijn positie te laten bereiken.
def Step1():
    GPIO.output(IN4, True)
    sleep (time)
    GPIO.output(IN4, False)

def Step2():
    GPIO.output(IN4, True)
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN4, False)
    GPIO.output(IN3, False)

def Step3():
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN3, False)

def Step4():
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)

def Step5():
    GPIO.output(IN2, True)
    sleep (time)
    GPIO.output(IN2, False)

def Step6():
    GPIO.output(IN1, True)
    GPIO.output(IN2, True)
    sleep (time)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)

def Step7():
    GPIO.output(IN1, True)
    sleep (time)
    GPIO.output(IN1, False)

def Step8():
    GPIO.output(IN4, True)
    GPIO.output(IN1, True)
    sleep (time)
    GPIO.output(IN4, False)
    GPIO.output(IN1, False)

# Linksom draaiing
def left(step):
	for i in range (step):
		#os.system('clear') # vertraagt de motorbewging te veel
		Step1()
		Step2()
		Step3()
		Step4()
		Step5()
		Step6()
		Step7()
		Step8()
		print "Step left: ",i

# Rechtsom draaiing
def right(step):
	for i in range (step):
		#os.system('clear') # vertraagt de motorbeweging te veel
		Step8()
		Step7()
		Step6()
		Step5()
		Step4()
		Step3()
		Step2()
		Step1()
		print "Step right: ",i

# Hier wordt de draairichting bepaald
if random.randint(0, 2) >= 1:
	# Hier komt tot stand hoe ver de motor draait
	left(random.randint(100, 1024))
else:
	# Hier komt tot stand hoe ver de motor draait
	right(random.randint(100, 1024))
GPIO.cleanup()
