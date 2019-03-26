#!/bin/bash

# input: .faa of unique genes

path_to_resfinder=../tools/resfinder/resfinder.py
path_to_victors_db=../tools/arg_dbs/victors
path_to_vfdb_db=../tools/arg_dbs/vfdb
path_to_blast=../tools/ncbi-blast-2.8.1+/bin/blast
path_to_rgi=../tools/rgi
v=0
path_to_clusters=../cluster/Cluster_faa/ProdigalCluster_95.fasta
path_to_fastas=../../gene_pred/Prodigal_results/nucleotides
path_to_python3=../tools/python3/Python-3.7.2/python
path_to_gffs=../../gene_pred/Prodigal_results/output
o=.

# o is out directory
while getopts "i:o:d:v" option
do
	case $option in
		i) path_to_clusters=$OPTARG;;
		o) o=$OPTARG;;
		v) v=1
	esac
done

mkdir -p "$o"/resfinder/gffs
for fasta in "$path_to_fastas"/*.fna
do
	file=$(basename "$fasta")
	[[ v -eq 1 ]] && echo "Running Resfinder for "$(basename "$file")
	sample=$(echo "$file" | sed 's/_.*//')
	mkdir -p "$o"/resfinder/"$sample"
	# "$path_to_python3" "$path_to_resfinder" -i "$fasta" -o "$o"/resfinder/"$sample" -p ~/db/resfinder_db/ -b "$path_to_blast"n
	awk -F "\t" 'BEGIN{OFS="\t"}{ print $6, "Resfinder", "ARD", $7, $7, ".", "strand", "frame", "resistance_gene_name=", $1, ";accession_no=", $9, ";phenotype=", $8}' "$o"/resfinder/"$sample"/results_tab.txt > "$o"/resfinder/"$sample"/almost.gff
	"$path_to_python3" gffmaker.py "$o"/resfinder/"$sample"/almost.gff "$path_to_gffs"/"$sample"_contigs.gff resfinder > "$o"/resfinder/gffs/"$sample"_resfinder.gff
done

