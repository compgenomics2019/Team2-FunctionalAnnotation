# headers: stitle qseqid sseqid sstart send qcovs bitscore score evalue sstrand
# YP_002228054.1 oxaloacetate decarboxylase [Salmonella enterica subsp. enterica serovar Gallinarum str. 287/91]	CGT2006_NODE_7_length_228456_cov_26.236566_198	YP_002228054.1	1	248	100	518	1333	0.0	N/A
# >CGT2006_NODE_7_length_228456_cov_26.236566_198 # 227712 # 228455 # 1 # ID=7_198;partial=01;start_type=ATG;rbs_motif=GGAGG;rbs_spacer=5-10bp;gc_cont=0.624
# seqid source type start end score strand phase attributes


def convert_to_gff():
	opref = {}
	with open("/projects/team2/func_annotation/operon/operon_ref.fasta",'r') as ref_file:
		for line in ref_file:
			if line.startswith('>'):
				line = line.strip()
				line = line.split(' ')
				tmp = ' '.join(line[1:])
				key = str(line[0])[1:]
				opref[key] = tmp

	input_ref = {}
	with open("./Cluster_path2fastafile",'r') as input_file:
		for line in input_file:
			if line.startswith('>'):
				line = line.strip()
				line = line.split(' ')
				tmp = [line[2],line[4]]
				key = str(line[0])[1:]
				input_ref[key] = tmp

	gff = {}
	with open("./operon_final_result/operon_output",'r') as output_file:
		for line in output_file:
			line = line.strip()
			line = line.split('\t')
			if line[1] not in gff.keys():
				gff[line[1]] = [line[1],"DOOR","operon annotation",input_ref[line[1]][0],input_ref[line[1]][1],line[-2],'.','.',opref[line[2]]]
		#print(gff)

	with open("./operon_final_result/97_operon.gff","w") as gff_file:
		for key in gff.keys():
			line = '\t'.join(gff[key])
			gff_file.write(line)
			gff_file.write('\n')




















