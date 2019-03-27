#!/bin/bash

team2=../../../team2
tools="$team2"/func_annotation/tools
path_to_resfinder="$tools"/resfinder/resfinder.py
path_to_dbs="$tools"/arg_dbs
path_to_blast="$tools"/ncbi-blast-2.8.1+/bin/blast
path_to_python3="$tools"/python3/Python-3.7.2/python

path_to_clusters="$team2"/func_annotation/cluster/Cluster_faa/ProdigalCluster_95.fasta
path_to_fastas="$team2"/gene_pred/Prodigal_results/nucleotides
path_to_gffs="$team2"/gene_pred/Prodigal_results/output
outdir=.
v=0

usage="$(basename "$0") [-h]
	-i <path_to_input_clusters>
	-o <path_to_output_directory>
	-g <path_to_prodigal_GFFs>
	-v (verbose mode)"
# input: .faa of unique genes
# o is out directory
while getopts "i:o:g:f:vh" option
do
	case $option in
		i) path_to_clusters=$OPTARG;;
		o) outdir=$OPTARG;;
		g) path_to_gffs=$OPTARG;;
		v) v=1;;
		h) echo "$usage"
		   exit;;
	esac
done

mkdir -p "$outdir"/resfinder/gffs
for fasta in "$path_to_fastas"/*.fna
do
	file=$(basename "$fasta")
	[[ v -eq 1 ]] && echo "Running Resfinder for "$(basename "$file")
	sample=$(echo "$file" | sed 's/_.*//')
	#mkdir -p "$outdir"/resfinder/"$sample"
	#"$path_to_python3" "$path_to_resfinder" \
	#	-i "$fasta" \
	#	-o "$outdir"/resfinder/"$sample" \
	#	-p "$path_to_dbs"/resfinder_db -b "$path_to_blast"n
	awk -F "\t" 'BEGIN{OFS="\t"}{
		print $6, "Resfinder", "ARD", $7, $7, ".", ".", ".",
		"hit_name="$1";accession_no="$9";phenotype="$8;
		}' "$outdir"/resfinder/"$sample"/results_tab.txt >> "$outdir"/resfinder/"$sample"/almost.gff
	"$path_to_python3" gffmaker.py \
		"$outdir"/resfinder/"$sample"/almost.gff \
		"$path_to_gffs"/"$sample"_contigs.gff \
		resfinder \
		> "$outdir"/resfinder/gffs/"$sample"_resfinder.gff
done

filend=$(echo "$path_to_clusters" | sed 's/.*\./\./')
infile=$(basename "$path_to_clusters" "$filend")

[[ v -eq 1 ]] && echo "Querying Victors database"
mkdir -p "$outdir"/victors
"$path_to_blast"p -query "$path_to_clusters" \
	-db "$path_to_dbs"/victors \
	-out "$outdir"/victors/victors_"$infile".out \
	-outfmt "6 qseqid sseqid length pident qcovs qstart qend sstart send evalue stitle" \
	-max_target_seqs 1 \
	-evalue 0.001
echo "##gff-version 3" > "$outdir"/victors/cluster_victors.gff
awk -F "\t" '{ if(($4 >= 90) && ($5 >= 90)) {
	print } }' "$outdir"/victors/victors_"$infile".out > "$outdir"/victors/victors_"$infile"_90.tsv
awk -F "\t" 'BEGIN{OFS="\t"}{ print $1, "Victors", "ARD", ".", ".", $10, ".", ".",
	"hit_id="$2";hit_name="$11}' "$outdir"/victors/victors_"$infile"_90.tsv >> "$outdir"/victors/cluster_victors.gff

[[ v -eq 1 ]] && echo "Querying VFDB"
mkdir -p "$outdir"/vfdb
"$path_to_blast"p -query "$path_to_clusters" \
	-db "$path_to_dbs"/vfdb \
	-out "$outdir"/vfdb/vfdb_"$infile".out \
	-outfmt "6 qseqid sseqid length pident qcovs qstart qend sstart send evalue stitle" \
	-max_target_seqs 1 \
	-evalue 0.001
echo "##gff-version 3" > "$outdir"/vfdb/cluster_vfdb.gff
awk -F "\t" '{ if(($4 >= 90) && ($5 >= 90)) {
	print } }' "$outdir"/vfdb/vfdb_"$infile".out > "$outdir"/vfdb/vfdb_"$infile"_90.tsv
awk -F "\t" 'BEGIN{OFS="\t"}{ print $1, "VFDB", "Virulence Factors", ".", ".", $10, ".", ".",
	"hit_id="$2";hit_name="$11}' "$outdir"/vfdb/vfdb_"$infile"_90.tsv >> "$outdir"/vfdb/cluster_vfdb.gff

[[ v -eq 1 ]] && echo "Running RGI"
mkdir -p "$outdir"/rgi
"$tools"/rgi main -i "$path_to_clusters" -o "$outdir"/rgi/rgi_"$infile" -t protein --clean
sed 's/;/,/g' "$outdir"/rgi/rgi_"$infile".txt > "$outdir"/rgi/rgi_"$infile"_nosemi.txt
echo "##gff-version 3" > "$outdir"/rgi/cluster_rgi.gff
awk -F "\t" 'BEGIN{OFS="\t"}{ print $1, "RGI", "ARD", "start", "end", ".", "strand", "frame", 
	"hit_name="$1";ARO_accession="$11";drug_class="$15";gene_family="$17;
	}' "$outdir"/rgi/rgi_"$infile"_nosemi.txt >> "$outdir"/rgi/cluster_rgi.gff
