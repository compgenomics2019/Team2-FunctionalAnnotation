#!usr/bin/bash

for i in ~/input_results/Prodigal_results/proteins/*.faa; do 
 ~/signalp-5.0/bin/signalp -fasta $i -org gram- -format short -gff3
done
for f in *.gff3; do mv -- "$f" "signalp_$f" ; done


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

sed -ir 's/^.*PredHel=0.*//' *.tmhmm
sed -i '/^$/d' *.tmhmm
for f in *.gff; do mv -- "$f" "tmhmm_$f" ; done




