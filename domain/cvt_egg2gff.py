#!usr/bin/python

# Usage: cvt_egg2gff.py reference.fasta eggNOG_results_file

import sys,re

def read_reference_file(filename):
    list_reference = []
    with open(filename,'r') as f:
        for line in f:
            if re.match('>',line):
                list_temp = [None]*9
                list_temp[0] = line.split()[0][1:]
                list_temp[1] = 'eggNOG:4.5'
                list_temp[2] = 'protein_match'
                list_temp[3] = line.split()[2]
                list_temp[4] = line.split()[4]
                list_temp[5] = 'evalue'
                if line.split()[6] == '1':
                    list_temp[6] = '+'
                elif line.split()[6] == '-1':
                    list_temp[6] = '-'
                list_temp[7] = '.'
                list_reference.append(list_temp)
    f.close()
    return list_reference

def read_eggNOG_file(filename):
    list_eggNOG = []
    with open(filename,'r') as f:
        for line in f:
            list_temp = [None]*9
            list_temp[0] = line.split('\t')[0]
            list_temp[5] = line.split('\t')[2]
            list_temp[8] = ';Gene=' + line.split('\t')[4] + ';Annot=' + line.split('\t')[-1].strip() 
            if line.split('\t')[5] != '':
                list_temp[8] = list_temp[8] + ';GO_terms=' + line.split('\t')[5]
            if line.split('\t')[6] != '':
                list_temp[8] = list_temp[8] + ';KEGG_KOs=' + line.split('\t')[6]
            if line.split('\t')[7] != '':
                list_temp[8] = list_temp[8] + ';BiGG_reactions=' + line.split('\t')[7]
            list_eggNOG.append(list_temp)
    f.close()
    return list_eggNOG

def main():

    file_reference = sys.argv[1]
    file_eggNOG = sys.argv[2]

    list_reference = read_reference_file(file_reference)
    list_eggNOG = read_eggNOG_file(file_eggNOG)

    for i in range(len(list_reference)):
        for annotation in list_eggNOG:
            if annotation[0] == list_reference[i][0]:
                list_reference[i][5] = annotation[5]
                list_reference[i][8] = annotation[8]
    
    with open('final_results_from_eggNOG_97.gff','w') as f:
        for line in list_reference:
            f.write('\t'.join(map(str,line)))
            f.write('\n')
    f.close()

if __name__ == '__main__':
    main()
