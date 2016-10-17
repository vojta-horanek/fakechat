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
w(0.5)
m("Mám problém")
i()
w(3)
m("Našli mě")
i()
w(4)
m("Bohužel nedělám, prý mi hrozí až 3 roky!")
i()
w(2)
m("No to teda!")
w(20)
