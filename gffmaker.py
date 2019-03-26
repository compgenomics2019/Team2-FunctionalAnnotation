import sys

output = sys.argv[1]	# almost gff path
gff = sys.argv[2]	# prev gff path
typ = sys.argv[3]	# file type
#output = 'test.tsv'	# almost gff path
#gff = 'CGT2006_contigs.gff'	# prev gff path
#typ = 'resfinder'	# file type

# key should match col 1 in gff + _iterator
def restogff():
	hits = {x.split('\t')[0].split()[0]:x.split('\t') for x in open(output).readlines()[1:]}
	nodes_with_hits = list(set([x.rsplit('_',1)[0] for x in hits.keys()]))
	
	outlines = []
	
	for line in open(gff):
		line = line.split('\t')
		if line[0] not in nodes_with_hits: continue
		seq_id = f'{line[0]}_{line[8].split(";")[0].split("_")[-1]}'
		if seq_id not in hits: continue
		# add GFF start to start position
		hits[seq_id][3] = str(int(hits[seq_id][3].split('..')[0]) + int(line[3]))
		hits[seq_id][4] = str(int(hits[seq_id][4].split('..')[-1]) + int(line[4]))
		hits[seq_id][6] = line[6]
		hits[seq_id][7] = line[7]
		outgff = hits[seq_id][:7]
		outgff.append(''.join(hits[seq_id][7:]))
		outlines.append('\t'.join(outgff))
	
	with open(gff) as f:
		for i in range(2): print(f.readline().strip())
	for x in outlines: print(x.strip())

def blasttogff():
	pass

def rgitogff():
	pass

if typ == 'resfinder': restogff()
elif typ == 'blast_tab': blasttogff()
elif typ == 'rgi': rgitogff()