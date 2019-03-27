#!/usr/bin/env python3

import sys
import os
import re
import subprocess
import argparse
from domain.interpro_annotation import annotation_interproscan
from domian.eggNOG_annotataion import eggnog_act
from domian.cvt_egg2gff import convert_eggnog
from domian.interpro_post_acts import interproscan_modify
from cluster.clustering_and_mapping import relabel, mapping_back, merge
from domain.annotaion_one_line import ol_act

def main():
    parser = argparse.ArgumentParser(description='Functional annotation')
    parser.add_argument('-i', '--input',  help='Input directory with 50 fna file', default=sys.stdin, type=str, required=True)
    parser.add_argument('-e', '--eggnog', help='Search against eggnog', default=False)
    parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')
    parser.add_argument('-ol', '--one_line', help='One line annotation with gene names', action='store_true')
    args = parser.parse_args()

    #Generate cluster fasta file and uc file
    Input_directory = args.input
    Cluster_path = './Cluster'
    Cluster_path2fastafile, Cluster_path2ucfile = relabel(Input_directory, Cluster_path)
    Dir_cluster = []
    Dir_merge = []

    if args.verbose:
        print("Interproscan is running for domain analysis")
    os.system('mkdir ./Interproscan')
    Dir_cluster.append('./Interproscan')
    output_for_interproscan = './Interproscan/97_interpro.gff'
    output_for_final = './Interproscan/97_interpro_trimmed.gff'
    annotation_interproscan(Cluster_path2fastafile,output_for_interproscan)
    interproscan_modify(Cluster_path2fastafile,output_for_interproscan,output_for_final)
    os.system('rm ./Interproscan/97_interpro.gff')

    if args.eggnog:
        if args.verbose:
            print("eggnog is running for domain analysis")
        os.system('mkdir ./EggNOG')
        Dir_cluster.append('./EggNOG')
        output_for_eggnog = './EggNOG/97_eggnog.gff'
        eggnog_act(Cluster_path2fastafile,output_for_eggnog)
        covert_eggnog(Cluster_path2fastafile,output_for_eggnog)

## ------------------------- Tool Script here -------------------------##
#  Cluster_path2fastafile is the cluster_centriod file
#  Input_directory is the Prodigal_fasta directory containing 50 faa file
#  I need the directory path you generate!!!!!!




## ------------------------- Tool Script end -------------------------##
    Output_gff_path = './Func_annotation_result'
    
    mapping_back(Dir_cluster, Cluster_path, Output_gff_path)
    merge(Dir_merge, Output_gff_path)

## ------------------------- One Line Annotation ---------------------##
    if args.one_line:
        os.system('ls ./Func_annotation_result/* > ./gff_reference')
        os.system('ls' + Input_directory + '/* > ./fastas')

        file_reference = "./gff_reference"
        path = "./Annotated_fastas"
        file_fastas = "./fastas"

        ol_act(file_reference,file_fastas,path)

        os.system('rm ./gff_reference')
        os.system('rm ./fastas')

if __name__ == "__main__":
    main()
