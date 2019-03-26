#!/usr/bin/env python3

import sys
import os
import re
import subprocess
import argparse
#from domain import cvt_egg2gff,eggNOG_annotataion,interpro_annotation,interpro_post_acts,annotation_one_line
from cluster.clustering_and_mapping import relabel, mapping_back, merge

def main():
    parser = argparse.ArgumentParser(description='Functional annotation')
    parser.add_argument('-i1', '--input1',  help='Input directory with 50 faa file', default=sys.stdin, type=str, required=True)
    parser.add_argument('-i2', '--input2',  help='Input directory with 50 fna file', default=sys.stdin, type=str, required=True)
    # parser.add_argument('-c', '--cluster',  help='Use the cluster file as inputs (.fasta)', type=str, required=True)
    parser.add_argument('-e', '--eggnog', help='Search against eggnog', default=False)
    # parser.add_argument('-m', '--mapping', help='Mapping back to each sample', type=str)
    parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')
    args = parser.parse_args()

    #Generate cluster fasta file and uc file
    Input_directory = args.input1
    fna_directory = args.input2
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





if __name__ == "__main__":
    main()
