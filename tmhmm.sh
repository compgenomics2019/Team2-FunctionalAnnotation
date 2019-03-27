for i in /projects/team2/gene_pred/Prodigal_results/proteins/*.faa; do 
#echo $i
#stripping of the path
filename="${i##*/}" 
#echo $filename
#stripping of the extension
basename="${filename%.[^.]*}"
#echo $basename
cat $i | /projects/team2/func_annotation/tools/tmhmm-2.0c/bin/tmhmm --short > ${basename}.tmhmm
done

sed -ir 's/^.*PredHel=0.*//' *.tmhmm
sed -i '/^$/d' *.tmhmm

mkdir tmhmm

python pythontmhmmgff.py



