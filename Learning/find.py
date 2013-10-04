#!/usr/bin/env python
# encoding: utf-8 #
# Simple imitation of the Unix find command, which search sub-tree
# for a named file, both of which are specified as arguments.
# Because python is a scripting language, and because python
# offers such fantastic support for file system navigation and
# regular expressions, python is very good at for these types # of tasks

from sys import argv
from os import listdir
from os.path import isdir, exists, basename, join
# import re

def listAllExactMatches(path, filename):
	"""Recursive function that lists all files matching the specified file name"""
	if(basename(path) == filename):
		# print(re.match(filename, basename(path)))
		print("Find: ",path)
	# match file by extension.
	# if(basename(path).endswith(".py")):
	# 	print("match:", path)
	if(not isdir(path)):
		print("not a path:",path)
		return
	dirlist = listdir(path)
	for file in dirlist:
		listAllExactMatches(file, filename)

def parseAndListMatches():
	"""Parses the command line, confirming that there are in fact three arguments, confirms that the specified 
	path is actually the name of a real directory, and then recursively searches the file tree rooted at the specified directory."""
	if(len(argv) != 3):
		print("Usage: find <path-to-directory-tree> <filename>")
		return
	directory = argv[1]
	if(not exists(directory)):
		print("Specified path ", directory," does not exist.")
		return
	if (not isdir(directory)):
		print (directory , "exists, but doesn't name an actual directory.") 
		filename = argv[2]
	listAllExactMatches(directory, filename)

# test code
listAllExactMatches("/Users/zhezhang/Documents/MyGitProjects/PythonCodes/", "find.py")

