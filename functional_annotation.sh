#!/bin/bash

usage="$(basename "$0") [-h]
    -i <path_to_input_cluster>
    -o <path_to_output_directory>
    -g <path to prodigal_GFFs>
    -v (verbose mode)"


while getopts "i:o:g:f:vgh" option
do 
    case $option in
        i) path_to_cluster=$OPTARG;;
        o) outdir=$OPTARG;;
        g) path_to_gffs=$OPTARG;;
        v) v=1;;
        h) echo $usage 
            exit;;
    esac
done

if [ ! -v ]; then 
    echo "doing SignalP"
    exit 1

for i in /projects/team2/gene_pred/Prodigal_results/proteins/*.faa; do 
 ~/signalp-5.0/bin/signalp -fasta $i -org gram- -format short -gff3
done

#in case one wants to add the prefix signalp to the file
#for f in *.gff3; do  mv -- "$f" "signalp_$f" ; done
mkdir spoutput
mv *.gff3 ./spoutput

echo "doing TM-HMM"

for i in /projects/team2/gene_pred/Prodigal_results/proteins/*.faa; do 
#echo $i
#stripping of the path
filename="${i##*/}" 
#echo $filename
#stripping of the extension
basename="${filename%.[^.]*}"
#echo $basename
cat $i | ~/tmhmm-2.0c/bin/tmhmm --short > ${basename}.tmhmm
done

sed -ir 's/^.*PredHel=0.*//' *.tmhmm
sed -i '/^$/d' *.tmhmm

#in case one wants to add the prefix to the file
#for f in *.gff; do mv -- "$f" "tmhmm_$f" ; done

#this step is to convert the output of tmhmm to gff

python ./tm/pythontmhmmgff.py


