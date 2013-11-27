#!/usr/bin/env python
# encoding: utf-8
# Split big data file into small files.


import fileinput
from random import randrange
# from sys import argv
# from os import listdir
# from os.path import isdir, exists, basename, join

def splitFiles(inputfilepath,desfilepath):
    """Split into files"""
    with fileinput.input(files=(inputfilepath)) as f:
        for line in f:
        	i_data = line.split(" ")
        	for i in i_data:
        		isIntValue = checkIntNumber(i)
        		if(isIntValue == True and i != "\n"):
        			process(i,desfilepath)
        		    # desfullfilepath = desfilepath + "_" +str(i%10)
        		    # appendDataToFile(str(i),desfullfilepath)
                
    print("splitFiles done!")

def process(data,desfilepath):
	# print(line)
	desfullfilepath = str(desfilepath) + "data_" + str(int(data) % 10) + ".dat"
	# print(desfullfilepath)
	appendDataToFile(str(data),desfullfilepath)

def checkIntNumber(userinput):
    try:
    	val = int(userinput)
    	return True
    except ValueError:
        print("That's not an int!" + userinput)
        return False

def generateDataFile(num, seed, srcfilepath):
	"""generate data  file of int data by random func"""
	with open(srcfilepath, mode='a', encoding='utf-8') as d_file:
		for x in range(1, num+1):
			d_file.write(str(randrange(seed)) + " ")
			if(x%10 == 0):
				d_file.write("\n")

def appendDataToFile(data, srcfilepath):
	with open(srcfilepath, mode='a', encoding='utf-8') as d_file:
		d_file.write(str(data) + " ")


# splitFiles("/Users/zhezhang/Documents/MyGitProjects/PythonCodes/find.py")
generateDataFile(20, 50000000,'bigdata_file.dat')
splitFiles("/Users/zhezhang/Documents/MyGitProjects/PythonCodes/BigData/bigdata_file.dat", "/Users/zhezhang/Documents/MyGitProjects/PythonCodes/BigData/")


