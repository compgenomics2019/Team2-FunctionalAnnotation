#!/usr/bin/env python3

import sys
import os
import re
import subprocess
import argparse
from domain.interpro_annotation import annotation_interproscan
from domain.eggNOG_annotation import eggnog_act
from domain.cvt_egg2gff import convert_eggnog
from domain.interpro_post_acts import interproscan_modify
from cluster.clustering_and_mapping import relabel, mapping_back, merge
from domain.annotation_one_line import ol_act
from sp.signalprun import signalP_finding
from sp.signalprun import signalP_finding
from tm.pythontmhmmgff import tmhmm_act
from crt.CRT import crt_act
from crt.convert_crt_to_gff import convert_crt


def main():
    parser = argparse.ArgumentParser(description='Functional annotation')
    parser.add_argument('-i', '--input',  help='Input directory with 50 fna file', default=sys.stdin, type=str, required=True)
    parser.add_argument('-ni', '--nucleotide_input',  help='Input directory with fna files', type=str,, default=False)
    parser.add_argument('-e', '--eggnog', help='Search against eggnog', default=False)
    parser.add_argument('-sp','--signalP', help='Running signalP to annotate signal peptide', default=False)
    parser.add_argument('-tm','--tmprotein', help='Running tmhmm to annotate transmembrane proteins', default=False)
    parser.add_argument('-crt','--crispr', help='Running CRISPR annotatation', default=False)
    parser.add_argument('-ard','--antibiotic', help='Running antibiotic annotatation', default=False)
    parser.add_argument('-ol','--one_line', help='One line annotation with gene names', action='store_true')
    parser.add_argument('-v', '--verbose', help='Verbose mode', default=False)
    
    args = parser.parse_args()


    #Generate cluster fasta file and uc file
    Input_directory = args.input
    Cluster_path = './Cluster'
    Cluster_path2fastafile, Cluster_path2ucfile = relabel(Input_directory, Cluster_path)
    Dir_cluster = []
    Dir_merge = []
    Dir_merge.append('./Prod_RNA_Results')                                                                                                  
    if args.verbose:                                                                                                                        
        print("Interproscan is running for domain analysis") 
    os.system('mkdir ./Interproscan')
    Dir_cluster.append('./Interproscan')
    output_for_interproscan = './Interproscan/97_interpro.gff'                                                                             
    output_for_final = './Interproscan/97_interpro_trimmed.gff'                                                                            
#     print(Cluster_path2fastafile,output_for_interproscan)                                                                                  
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
        convert_eggnog(Cluster_path2fastafile,output_for_eggnog) 

## ------------------------- Tool Script here -------------------------##
#  Cluster_path2fastafile is the cluster_centriod file
#  Input_directory is the Prodigal_fasta directory containing 50 faa file
    
    # Signal peptide annotation
    
    if args.signalP:
        if args.verbose:
            print("signalP is running for signal peptide annotation")
        signalP_finding(Input_directory)
        Dir_merge.append('./signalp')
        
    # Transmembrane protein annotation
    
    if args.tmprotein:
        if args.verbose:
            print("tmhmm is running for transmembrane protein annotation")
        os.system("bash ./tm/tmhmm.sh " + Input_directory)
        Dir_merge.append('./tmhmm')
        
    # CRISPR annotation
    
    if args.crispr:
        if args.nucleotide_input:
            if args.verbose:
                print("CRISPR annotation is running")
            crt_act(args.nucleotide_input)
            convert_crt(args.nucleotide_input)   
        else: print("nucleotide fna needed")
            
     # Antibiotic resistence annotation
    
    if args.antibiotic:
        clustered_file = Cluster_path2fastafile
        ard_output = "./ard_results"
        os.system("mkdir ./ard_results")
        os.system("bash ./ard/ard_run.sh -i " + clustered_file + " -o " + ard_output)
        
        
## ------------------------- Tool Script end -------------------------##
    Output_gff_path = './Func_annotation_result'
    
    mapping_back(Dir_cluster, Cluster_path, Output_gff_path)
    merge(Dir_merge, Output_gff_path)

## ------------------------- One Line Annotation ---------------------##
    if args.one_line:                                                                                                                       
        os.system('ls ./Func_annotation_result/* > ./gff_reference')                                                                        
        os.system('ls ' + Input_directory + '/* > ./fastas')                                                                                
                                                                                                                                            
        file_reference = "./gff_reference"                                                                                                  
        file_fastas = "./fastas"                                                                                                            
                                                                                                                                            
        ol_act(file_reference,file_fastas)                                                                                                  
                                                                                                                                            
        os.system('rm ./gff_reference')                                                                                                     
        os.system('rm ./fastas')                                                                                                            
                                                                                                                                            
if __name__ == "__main__":                                                                                                                  
    main()       
