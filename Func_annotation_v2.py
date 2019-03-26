import os
import sys
import re
import copy

# Take the result from prodigal protein
relabel_file = []
for file in os.listdir("./Prodigal_protein"):
	if file.endswith(".faa"):
		relabel_file .append(file)


# Relabel the contig files and generate Relabel directory with relabel contig files
os.mkdir('./Relabel', 0755)
path = './Prodigal_protein'
for FileName in relabel_file:
	InFile = open(path + '/' + FileName, 'r')
	OutFile = open('./Relabel/' + FileName, 'w')
	Label = re.split(';|\.|_|/',FileName)[-3]
	pattern = re.compile("^>")
	for line in InFile:
		if pattern.match(line):
			line = line[:1] + Label + '_' + line[1:]
		OutFile.write(line)
	InFile.close()
	OutFile.close()

# Merge the relabel file togethor and Run Uclust command line in Cluster directory
os.mkdir('./Cluster', 0755)
os.system('cat ./Relabel/* > ./Cluster/All_Prodigal.faa')
os.system('usearch -cluster_fast ./Cluster/All_Prodigal.faa -id 0.97 -centroids ./Cluster/ProdigalCluster_97.fasta -uc ./Cluster/ProdigalCluster_97.uc')


# Every one's script





# Mapping clusters back to contig and create Func_annotation_result directory with all the gff file

d = {}
for file in os.listdir("./Relabel"):
	if file.endswith(".faa"):
		file = file.split('_')[0]
		d[file] = []

for file in os.listdir("./Cluster"):
	if file.endswith(".uc"):
		cluster_file = file

f = open("./Cluster/" + cluster_file, 'r')
Pos_map = {}
cluster = {}
for line in f:
	lines = line.strip().split('\t')
	if lines[0] == 'S':
		data = lines[8].split(' ')
		lines[8] = data[0]
		cluster[lines[8]] = []
		if lines[8] not in Pos_map:
			Pos_map[lines[8]] = (data[2], data[4])
	elif lines[0] == 'H':
		data = lines[8].split(' ')
		lines[8] = data[0]
		lines[9] = lines[9].split(' ')[0]
		cluster[lines[9]].append(lines[8])
		if lines[8] not in Pos_map:
			Pos_map[lines[8]] = (data[2], data[4])


#change here with only the cluster result directory
dirs = ['./eggNOG', './interproscan', './operon']
#dirs = [ name for name in os.listdir('./') if os.path.isdir(os.path.join('./', name)) ]

gff_files = []
for dir in dirs:
	gff_files += [('./' + dir + '/' + name) for name in os.listdir('./' + dir) if name.endswith(".gff")]

for gff in gff_files:
	f = open(gff, 'r')
	for line in f:
		lines = line.strip().split('\t')
		contig = lines[0].split('_')[0] #CGT2006
		if contig in d:
			pos = lines[0].find('_')
			temp = copy.deepcopy(lines)
			#add this two line
			temp[3] = Pos_map[temp[0]][0]
			temp[4] = Pos_map[temp[0]][1]
			#--------------			
			temp[0] = temp[0][pos+1:]
			d[contig].append('\t'.join(temp) + '\n')
			if cluster[lines[0]]:
				for elem in cluster[lines[0]]:
					lines[0] = elem
					contig = lines[0].split('_')[0] #CGT2010
					pos = lines[0].find('_')
					lines[3] = Pos_map[lines[0]][0]
					lines[4] = Pos_map[lines[0]][1]
					lines[0] = lines[0][pos+1:]
					d[contig].append('\t'.join(lines) + '\n')
	f.close()

path = './Func_annotation_result'
os.mkdir(path, 0755)
for key, values in sorted(d.items(), key = lambda x:x[0], reverse = False):
	filename = path + '/' + key + '.gff'
	f = open(filename, 'w')
	f.write('##gff-version  3\n')
	for value in values:
		f.write(value)

# merge ncRNA and sigIP
merge_dir = ['./Prod_RNA_Results', './signalpgff3']
for dir in merge_dir:
	for file in os.listdir(dir):
		contig = file.strip().split('_')[0]
		filename = path + '/' + contig + '.gff'
		os.system('grep -v "^#" ' + dir + '/' + file + '>>' + filename)
