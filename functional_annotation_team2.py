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
from sp.signalprun import signalP_finding
from tm.pythontmhmmgff import tmhmm_act

def main():
    parser = argparse.ArgumentParser(description='Functional annotation')
    parser.add_argument('-i', '--input',  help='Input directory with faa files', default=sys.stdin, type=str, required=True)
    parser.add_argument('-ni', '--nucleotide_input',  help='Input directory with fna files', type=str)
    parser.add_argument('-e', '--eggnog', help='Search against eggnog', default=False)
    parser.add_argument('-sp','--signalP', help='Running signalP to annotate signal peptide', default=False)
    parser.add_argument('-tm','--tmprotein', help='Running tmhmm to annotate transmembrane proteins', default=False)
    parser.add_argument('-ol','--one_line', help='One line annotation with gene names', action='store_true')
    parser.add_argument('-v', '--verbose', help='Verbose mode', default=False)
    parser.add_argument('-h','--help', help='Print usage',  default=False)
    
    args = parser.parse_args()

    # Usage
    if args.help:
        print("Usage: functional_annotation_team2.py -i <input_dicrectory> [options]\n",
              "-i\t--input\tInput directory with faa files\n",
              "-ni\t--nucleotide_input\tInput directory with fna files\n",
              "-e\t--eggnog\tSearch against eggnog[optional]\n",
              "-sp\t--signalP\tRunning signalP to annotate signal peptide[optional]\n",
              "-tm\t--tmprotein\tRunning tmhmm to annotate transmembrane proteins[optinal]\n",
              "-ol\t--one_line\tOne line annotation with gene names[Ture or False]\n",
              "-v\t--verbose\tVerbose mode\n",
              "-h\t--help\tPrint usage\n")
    
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
    
    # Signal peptide annotation
    
    if args.signalP:
        signalP_finding(Input_directory)
        
    # Transmembrane protein annotation
    
    if args.tmprotein:
        tmhmm_act(Input_directory)
        
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
