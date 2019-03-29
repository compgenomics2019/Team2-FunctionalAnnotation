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
from cluster.clustering_and_mapping import merge_file_map, relabel, mapping_back, merge
from domain.annotation_one_line import ol_act
from sp.signalprun import signalP_finding
from sp.signalprun import signalP_finding
from crt.CRT import crt_act
from crt.convert_crt_to_gff import convert_crt
from bedtools_scripts.bedtools_sort import sort
from operon.get_gff import convert_to_gff

def main():
    parser = argparse.ArgumentParser(description='Functional annotation')
    parser.add_argument('-i', '--input',  help='Input directory with 50 fna file', default=sys.stdin, type=str, required=True)
    parser.add_argument('-ni', '--nucleotide_input',  help='Input directory with fna files', type=str, default=False)
    parser.add_argument('-e', '--eggnog', help='Search against eggnog', default=False)
    parser.add_argument('-sp','--signalP', help='Running signalP to annotate signal peptide', default=False)
    parser.add_argument('-tm','--tmprotein', help='Running tmhmm to annotate transmembrane proteins', default=False)
    parser.add_argument('-crt','--crispr', help='Running CRISPR annotatation', default=False)
    parser.add_argument('-ard','--antibiotic',help='Running antibiotic annotatation', default=False)
    parser.add_argument('-ol','--one_line', help='One line annotation with gene names', action='store_true')
    parser.add_argument('-v', '--verbose', help='Verbose mode', default=False)
    parser.add_argument('-op', '--operon', help='operon annotation', default=False)
    
    args = parser.parse_args()


    #Generate cluster fasta file and uc file
    Input_directory = args.input
    Cluster_path = './Cluster'
    Cluster_path2fastafile, Cluster_path2ucfile = relabel(Input_directory, Cluster_path)
#    Cluster_path2fastafile = './Cluster/ProdigalCluster_97_n.fasta'
    Dir_cluster = []
    Dir_merge = []
#     Dir_merge.append('./Prod_RNA_Results')                                                                                                  
    if args.verbose:                                                                                                                        
        print("Interproscan is running for domain analysis") 
    os.system('mkdir ./Interproscan')
    Dir_cluster.append('./Interproscan')
    output_for_interproscan = './Interproscan/97_interpro.gff'                                                                             
    output_for_final = './Interproscan/97_interpro_trimmed.gff'                                                                            
#    print(Cluster_path2fastafile,output_for_interproscan)                                                                                  
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
            
    # Antibiotic resistance annotation
    
    if args.antibiotic:
        if args.verbose:
                print("Ahttps://github.gatech.edu/compgenomics2019/Team2-FunctionalAnnotationnbiotic resistance annotation is running")
        os.system("chmod 755 ./ard/ard_run.sh")
        os.system("./ard/ard_run.sh -i " + Cluster_path2fastafile)
        Dir_cluster.append('./victors')
        Dir_cluster.append('./vfdb')
        Dir_cluster.append('./rgi')
      
    #Operon annotation
    if args.operon:
        if args.verbose:
                print("Operon annotation is running")
        os.system("/projects/team2/func_annotation/tools/ncbi-blast-2.8.1+/bin/makeblastdb -in /projects/team2/func_annotation/operon/operon_ref.fasta -dbtype prot")
        os.system("mkdir operon_final_result")
        os.system("chmod 755 operon_final_result")          
        os.system("/projects/team2/func_annotation/tools/blastp -db /projects/team2/func_annotation/operon/operon_ref.fasta -query " + Cluster_path2fastafile + " -num_threads 4 -evalue 1e-10 -outfmt "6 stitle qseqid sseqid sstart send qcovs bitscore score evalue sstrand" > ./operon_final_result/operon_output")
        convert_to_gff(Cluster_path2fastafile)  #output file: ./operon_final_result/97_operon.gff
        Dir_cluster.append('./operon_final_result')
        
        
        
## ------------------------- Tool Script end -------------------------##
    Output_gff_path = './Func_annotation_result'
    
    mapping_back(Dir_cluster, Cluster_path, Output_gff_path)
    Position_map = merge_file_map('./' + Input_directory)
    merge(Dir_merge, Output_gff_path, Position_map) 
#    merge(Dir_merge, Output_gff_path)


## ------------------------- Tool Script end -------------------------##
    for files in os.listdir('./Func_annotation_result'):
        files = './Func_annotation_result/' + files
        os.system('sort ' + files + ' > ' + files +'_sorted.gff')
        os.system('rm '+ files)

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
