#!/bin/bash


for i in $1/*.faa; do 
#echo $i
#stripping of the path
filename="${i##*/}" 
#echo $filename
#stripping of the extension
basename="${filename%.[^.]*}"
#echo $basename
cat $i | /projects/team2/func_annotation/tools/tmhmm-2.0c/bin/tmhmm --short > ${basename}.tmhmm
done

sed -i 's/^.*PredHel=0.*//' *.tmhmm
sed -i '/^$/d' *.tmhmm

mkdir tmhmm

/projects/team2/func_annotation/bin/python3/Python-3.7.2/python ./pythontmhmmgff.py

mv *.tmhmm ./tmhmm
mv *.gff ./tmhmm

rm -rf TMHMM_*

