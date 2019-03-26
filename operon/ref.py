import os
from Bio import Entrez
import urllib3

all_files = os.listdir("operon/")
txt_files = filter(lambda x: x[-4:] == '.opr', all_files)
ids = []
for file in txt_files:
	with open("operon/%s"%file,'r') as sub_file:
		for i in range(11):
			next(sub_file)
		for line in sub_file:
			try:
				line = line.strip("\n")
				line = line.split("\t")
				#print(line[1])
				ids.append(line[1])
			except:
				continue
	#print(ids)
# print(len(ids))
ids = list(set(ids))
# print(len(ids))
x = 0
n = 0
for i in ids:
	with open("new_ref/ref.fasta",'a') as file2:
		n+=1
		Entrez.email="jhgmjyf%f@gmail.com"%x
		handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id=i)
		tmp = handle.read()
		print(n)
		file2.write(tmp)
		x += 1
			