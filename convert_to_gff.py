#!/usr/bin/env python3


import sys
import subprocess
from os import listdir
from os.path import isfile, join
import re

inputDir = sys.argv[1]

inputfiles = [f for f in listdir(inputDir) if isFile(join(inputDir, f))]
for file1 in inputfiles:
	convert_to_gff(file1)
	outputfilename = file1.split(.)[0]+"gff"
	with open(outputfilename, w) as fr:
	fr.write(listfromfunction)

def convert_to_gff(inputfile):
	count = 0
	templist = [None]*9
	list1 = []
	startlist = [[], []]
	attributes = [[], [], []]
	with open("inputfile") as f:
        	lines = f.readlines()
        	for i in range(len(lines)):
			if re.findall(pattern = "^CRISPR", string = lines[i]):
				count+= 1
			for n in range(count):
				if re.match(pattern = "^ORGANISM:", string = lines[0]):
						templist[0] = lines[0].split()[1]
						templist[1] = "CRT1.2-CLI"
						templist[2] = "CRISPR"
					if re.findall(pattern = "^CRISPR", string = lines[i]):
						startlist[0].append(lines[i].split()[3])
						startlist[1].append(lines[i].split()[5])
						templist[3] = startlist[0][n]
						templist[4] = startlist[1][n]
						templist[5] = "."
						templist[6] = "+/-"
						templist[7] = "."			
					if re.findall(pattern="^Repeats", string = lines[i]):
						attributes[0].append(lines[i].split()[1])
						attributes[1].append(lines[i].split()[4])
						attributes[2].append(lines[i].split()[7])
						templist[8] = "rnum="+attributes[0][n]+", rlen="+attributes[1][n]+", slen="+attributes[2][n]
		#print(templist)


