#!/usr/bin/env python

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)
time.sleep(10.0)
#GPIO0
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, True)
time.sleep(2.0)
GPIO.output(11, False)

#GPIO1
GPIO.setup(12,  GPIO.OUT)
GPIO.output(12, True)
time.sleep(2.0)
GPIO.output(12, False)

#GPIO2
GPIO.setup(13,  GPIO.OUT)
GPIO.output(13, True)
time.sleep(2.0)
GPIO.output(13, False)

#GPIO3
GPIO.setup(15,  GPIO.OUT)
GPIO.output(15, True)
time.sleep(2.0)
GPIO.output(15, False)

#GPIO4
GPIO.setup(16,  GPIO.OUT)
GPIO.output(16, True)
time.sleep(2.0)
GPIO.output(16, False)

#GPIO5
GPIO.setup(18,  GPIO.OUT)
GPIO.output(18, True)
time.sleep(2.0)
GPIO.output(18, False)

#GPIO6
GPIO.setup(22,  GPIO.OUT)
GPIO.output(22, True)
time.sleep(2.0)
GPIO.output(22, False)

#GPIO7
GPIO.setup(7,  GPIO.OUT)
GPIO.output(7, True)
time.sleep(2.0)
GPIO.output(7, False)

