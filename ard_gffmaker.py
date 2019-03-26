import sys

almost_gff = sys.argv[1]	# almost gff path
gff = sys.argv[2]	# prev gff path
typ = sys.argv[3]	# file type
#almost_gff = 'test.tsv'	# almost gff path
#gff = 'CGT2006_contigs.gff'	# prev gff path
#typ = 'resfinder'	# file type

# key should match col 1 in gff + _iterator
def restogff():
	hits = {x.split('\t')[0].split()[0]:x.split('\t') for x in open(almost_gff).readlines()[1:]}
	nodes_with_hits = list(([x.rsplit('_',1)[0] for x in hits.keys()]))	# set of nodes
	
	outlines = []
	
	for line in open(gff):
		line = line.split('\t')
		if line[0] not in nodes_with_hits: continue
		seq_id = f'{line[0]}_{line[8].split(";")[0].split("_")[-1]}'
		if seq_id not in hits: continue

		# add GFF START (offset) to start and end positions
		hits[seq_id][3] = str(int(hits[seq_id][3].split('..')[0]) + int(line[3]))
		hits[seq_id][4] = str(int(hits[seq_id][4].split('..')[-1]) + int(line[3]))

		# pull strand and frame directly from gff
		hits[seq_id][6] = line[6]
		hits[seq_id][7] = line[7]

		# join attributes into one field and generate output line
		outgff = hits[seq_id][:8]
		outgff.append(''.join(hits[seq_id][8:]))
		outlines.append('\t'.join(outgff))

	# get GFF headers
	with open(gff) as f:
		for i in range(2): print(f.readline().strip())
	for x in outlines: print(x.strip())

def blasttogff():
	hits = {x.split('\t')[0]:x.split('\t') for x in open(almost_gff).readlines()}
	nodes_with_hits = list(([x.rsplit('_',1)[0] for x in hits.keys()]))	# set of nodes
	
	outlines = []
	
	for line in open(gff):
		line = line.split('\t')
		if line[0] not in nodes_with_hits: continue
		seq_id = f'{line[0]}_{line[8].split(";")[0].split("_")[-1]}'
		if seq_id not in hits: continue

		# add GFF START (offset) to start and end positions
		hits[seq_id][3] = str(int(hits[seq_id][3]) + int(line[3]))
		hits[seq_id][4] = str(int(hits[seq_id][4]) + int(line[3]))

		# pull strand and frame directly from gff
		hits[seq_id][6] = line[6]
		hits[seq_id][7] = line[7]

		# join attributes into one field and generate output line
		outgff = hits[seq_id][:8]
		outgff.append(''.join(hits[seq_id][8:]))
		outlines.append('\t'.join(outgff))

def rgitogff():
	hits = {x.split('\t')[0].split()[0]:x.split('\t') for x in open(almost_gff).readlines()[1:]}
	nodes_with_hits = list(([x.rsplit('_',1)[0] for x in hits.keys()]))	# set of nodes
	
	outlines = []
	
	for line in open(gff):
		line = line.split('\t')
		if line[0] not in nodes_with_hits: continue
		seq_id = f'{line[0]}_{line[8].split(";")[0].split("_")[-1]}'
		if seq_id not in hits: continue

		# pull start, end, strand and frame directly from gff
		hits[seq_id][3:8] = line[3:8]

		# join attributes into one field and generate output line
		outgff = hits[seq_id][:8]
		outgff.append(''.join(hits[seq_id][8:]))
		outlines.append('\t'.join(outgff))

	# get GFF headers
	with open(gff) as f:
		for i in range(2): print(f.readline().strip())
	for x in outlines: print(x.strip())


if typ == 'resfinder': restogff()
elif typ == 'blast': blasttogff()
elif typ == 'rgi': rgitogff()
