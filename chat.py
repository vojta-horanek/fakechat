#!usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import time
from random import randint

use_random_ip = "true" #changing this to false will use the ip addresses described below, default is true
ip1 = "84.246.186.0"
ip2 = "84.265.126.0"

#random ip addresses
number1 = randint(0,255)
number2 = randint(0,255)
number3 = randint(0,255)
number4 = randint(0,255)
#random ip addresses 2
number5 = randint(0,255)
number6 = randint(0,255)
number7 = randint(0,255)
number8 = randint(0,255)
def i():
	if (use_random_ip is "true"):
		raw_input("%d:%d:%d:%d : " % (number5, number6, number7, number8))
	else:
		raw_input("%s : " % ip2)
def w(timetosleep):
	time.sleep(timetosleep)
def m(str):
	if (use_random_ip is "true"):
		print ("%d:%d:%d:%d : %s" % (number1, number2, number3, number4, str))
	else:
		print ip1, ":", str		
#if the third argument is 1 there will be an input after the message
def f(message, time, input):
	m(message)
	if input == 1:
		i()
	w(time)
	
f("Hi!", 2, 1)
f("What's up?", 2, 1)
f("I'm doing great!", 2, 1)
f("Am i smart?", 2, 1)
