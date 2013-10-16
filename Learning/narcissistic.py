#!/usr/bin/env python
# encoding: utf-8
# Here's a simple script (feels like a program, though) that prints out
# the first n narcissistic numbers, where n is provided on the command line. import sys
import sys

def numDigits(num):
	"""Returns the number of digits making
	up a number, not counting leading zeroes,
	except for the number 0 itself."""
	if(num ==0): return 1
	digitCount = 0
	while(num > 0):
		digitCount += 1
		num /= 10
	return digitCount

def isNarcissistic(num):
	"""Returns True if and only if the number is a narcissistic number.""" 
	originalNum = num
	total = 0
	exp = numDigits(num)
	while(num>0):
		digits = num%10
		total += digits ** exp
		num /= 10
	return total == originalNum

def listNarcissisticNumbers(numNeeded):
	"""Searches for an prints out the first 'numNeeded' narcissistic numbers."""
	numFound = 0
	numToConsider = 0
	print ("here are  the first ", numNeeded, " narcissistic numbers.")
	while(numFound < numNeeded):		
		if(isNarcissistic(numFound)):
			numFound += 1
			print ("Find a Narcissistic number: ",numToConsider)
		numToConsider += 1
	print("Done!")	

def getNumberNeeded():
	numNeeded = 9; # this is the default number 
	if len(sys.argv) > 1:
		try:
			numNeeded = int(sys.argv[1])
		except ValueError:
			print ("Non-integral argument encountered... using default.")	
	return numNeeded

listNarcissisticNumbers(getNumberNeeded())
