import sys

almost_gff = sys.argv[1]	# almost gff path
gff = sys.argv[2]	# prev gff path
typ = sys.argv[3]	# file type

# key should match col 1 in gff + _iterator
hits = {x.split('\t')[0].split()[0]:x.split('\t') for x in open(almost_gff).readlines()[1:]}
nodes_with_hits = list(([x.rsplit('_',1)[0] for x in hits.keys()]))	# set of nodes

outlines = []

for line in open(gff):
	line = line.split('\t')
	if line[0] not in nodes_with_hits: continue
	seq_id = f'{line[0]}_{line[8].split(";")[0].split("_")[-1]}'
	if seq_id not in hits: continue

	# add GFF start and end positions
	hits[seq_id][3] = line[3]
	hits[seq_id][4] = line[4]

	# pull strand and frame directly from gff
	hits[seq_id][6] = line[6]
	hits[seq_id][7] = line[7]

	# join attributes into one field and generate output line
	outlines.append('\t'.join(hits[seq_id]))

# get GFF headers
print(open(gff).readline().strip())
for x in outlines: print(x.strip())
