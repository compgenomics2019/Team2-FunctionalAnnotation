#!/usr/bin/env python3

#Usage: ./convert_crt_to_gff.py <inputdirectory>
#In this case <inputdirectory> is /projects/team2/func_annotation/ncRNA_Results/Assembled_Contigs/CRT_results
def convert_crt(input_dir):
	import sys
	import subprocess
	from os import listdir,system
	from os.path import isfile, join
	import re

	#function to convert the crt output to gff file format
	def convert_crtout_to_gff(filename):
		list_reference = []
		f = open(filename, "r")
		lines = f.readlines()
		# print(lines)
		# with open(filename) as f:
			# lines = f.readlines()
		count = 0
		templist=[None]*9
		startlist = [[], []]
		attributes = [[], [], []]
		for i in range(len(lines)):
			if re.match(pattern = "^ORGANISM:", string = lines[0]):
				templist[0] = lines[0].split()[1]
				templist[1] = "CRT1.2-CLI"
				templist[2] = "CRISPR"
				templist[5] = "."
				templist[6] = "."
				templist[7] = "."
			if re.findall(pattern = "^CRISPR", string=lines[i]):
				count += 1
				startlist[0].append(lines[i].split()[3])
				startlist[1].append(lines[i].split()[5])
			if re.findall(pattern = "^Repeats", string = lines[i]):
				attributes[0].append(lines[i].split()[1])
				attributes[1].append(lines[i].split()[4])
				attributes[2].append(lines[i].split()[7])
		for n in range(0, count):
			list_reference.append([templist[0], templist[1], templist[2], startlist[0][n], startlist[1][n], templist[5], templist[6], templist[7], "rnum="+attributes[0][n]+", rlen="+attributes[1][n]+", slen="+attributes[2][n]])
		#print(list_reference)
		return list_reference

	#getting all the crt output files listed in directory
	inputDir = input_dir

	inputfiles = [f for f in listdir("./") ]
	system("mkdir ./CRISPR_results")
	for file1 in inputfiles:
		if "_crt.out" in file1:
			output = convert_crtout_to_gff(file1)
			outputfilename = file1.split(".")[0]+".gff"
			with open(outputfilename, 'w') as ofile:
				for line in output:
					ofile.write('\t'.join(map(str, line)))
					ofile.write('\n')
	system("mv *.gff ./CRISPR_resultst")
	system("rm *.out ")
