import os
all_files = os.listdir("/projects/team2/genome_assembly/dataset/")
txt_files = filter(lambda x: x[-3:] == '.fq', all_files)
n =0
for file in txt_files:
	print(n)
	n += 1
	if n > 18:
		name = file.split('.')
		name = name[0]
		os.system('perl plasmidseeker.pl -d ../db_w20 ' +"-i /projects/team2/genome_assembly/dataset/"+ file + " -b ../whole_genome.txt "  +'-o ./output' +name
	)





#/projects/team2/genome_assembly/dataset fq
