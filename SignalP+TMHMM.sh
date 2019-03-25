#!usr/bin/bash

for i in ~/input_results/Prodigal_results/proteins/*.faa; do 
 ~/signalp-5.0/bin/signalp -fasta $i -org gram- -format short -gff3
done

for i in ~/input_files/Prodigal_results/proteins/*.faa; do 
#echo $i
#stripping of the path
filename="${i##*/}" 
#echo $filename
#stripping of the extension
basename="${filename%.[^.]*}"
#echo $basename
cat $i | ~/tmhmm-2.0c/bin/tmhmm --short > ${basename}.tmhmm
done



