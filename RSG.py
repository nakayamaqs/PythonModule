#!/usr/bin/env python
# encoding: utf-8
# Script that generates three random sentences from the
# hard-code grammar. In general, the grammar would be
# stored in a data file, but to be honest, it would likely
# be encoded as a serialized dictionary, since that would make it
# trivial to deserialize the data.

import sys
from random import seed, choice

grammar = { '<start>': [['The ', '<object>', ' ', '<verb>', ' tonight.']],
		    '<object>': [['waves'], ['big yellow flowers'], ['slugs']],
		    '<verb>': [['sigh ', '<adverb>'], ['portend like ', '<object>']],
		    '<adverb>': [['warily'], ['grumpily']] }


# Expands the specified symbol into a string of terminals. If the symbol is already a terminal,
# then we just print it as is to sys.stdout. Otherwise,
# we look the symbol up in the grammar, choose a random expansion, and map the expand function over it.
# Note the mapping functionality that comes with map. Scheme has its influences, people!

def expand(symbol):
	if symbol.startswith('<'):
		options = grammar[symbol]
		production = choice(options)
		# print('production=',production, " islist:", isinstance(production,list))
		list(map(expand, production)) #should add list() for Python 3.3, using 3.1's map would be lazy evaluation when iterating on a complex function, large data sets, or streams
	else:
		sys.stdout.write(symbol)
		# print("www")

# Seeds the randomization engine, and the procceds to generate three random sentences.
# We use sys.stdout so we have a little more control over formatting.

def generateRandomSentences(numSentences):
	seed()
	for iteration in range(numSentences):
		sys.stdout.write(str(iteration + 1))
		sys.stdout.write('.) ')
		expand('<start>')
		sys.stdout.write('\n')

def printfunc(sth):
	print('88:',sth)

generateRandomSentences(3)
# list(map(printfunc, ['The ', '<object>', ' ', '<verb>', ' tonight.']))
# map(printfunc, ['The ', '<object>', ' ', '<verb>', ' tonight.'])
print(list(map(chr,[66,53,0,94])))
print(map(chr,[66,53,0,94]))
