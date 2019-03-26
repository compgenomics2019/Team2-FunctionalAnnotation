import os
from Bio import Entrez
import urllib3
from urllib.error import HTTPError
import json

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
print(len(ids))
# print(len(ids))
# ids = list(set(ids))
# # print(len(ids))
# x = 0
# #Entrez.email="jhgmjyf%f@gmail.com"%x
# n = 0
# y = 714
# errors= []
# for i in ids:
# 	with open("ref/ref_%f.fasta"%y,'a') as file2:
# 		n+=1
# 		# x += 1
# 		if n>87118:
# 			try:

# 				Entrez.email="ohkj%f@163.com"%x
# 				handle = Entrez.efetch(db="protein", rettype="fasta", retmode="text", id=i)
# 				tmp = handle.read()
# 				print(n)
# 				file2.write(tmp)
# 			# x += 1
# 			# y += 1
# 			except HTTPError:
# 				errors.append(i)
# 				print("error at:", n)

# with open("errors", "w") as f:
# 	json.dump(errors, f)









#2201
#2279
#3212 4
#1643 1
#1685 2
#7553 3
#9311 4
#10532 5
#17749 6
#17797 7
#20511 8
#22264 9
#25867 10
#29768 11
#30873 12
#31007 13
#33386 14
#33773 15
#33826 16
#34469 713
#46155
#57844
#61427
#62370
#64415
#64720
#65769
#65898
#66207
#66667#67388
#68206
#68286
#68351
#68677#69487
#69904#70318 70956 71582 71646 72042 72401 72570 73224