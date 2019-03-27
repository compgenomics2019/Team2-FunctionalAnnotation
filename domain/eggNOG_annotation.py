#!usr/bin/python 3

import sys 
from subprocess import Popen, PIPE

# Usage: eggNOG_annotation <input_file> <output_file>

def download_eggnog_database():

    # Before annotation, bactNOG database will be checked and installed

    process = Popen(args = ['python',           # This require python 2.7
                            '/projects/team2/func_annotation/tools/eggnog/eggnog_dataset/eggnog-mapper-1.0.3/download_eggnog_data.py', 
                            '-y',
                            'bact'],            # Download specific database for bacteria
                            stdout = PIPE, stderr = PIPE)
    stdout, stderr = process.communicate()
    print(stdout,stderr)
    del stdout,stderr

def annotation_eggnog(input_file,output_file):
    
    # Using diamond for fast and accurate annotation

    process = Popen(args = ['python',           # This require python 2.7
                            '/projects/team2/func_annotation/tools/eggnog/eggnog_dataset/eggnog-mapper-1.0.3/emapper.py', 
                            '-i',input_file,    
                            '-m','diamond',     # hmmer method can be replaced
                            '-o',output_file],
                            stdout = PIPE, stderr = PIPE)
    stdout, stderr = process.communicate()
    print(stdout,stderr)
    del stdout,stderr

def eggnog_act(intput,output):
    input_file = input
    output_file = output

    download_eggnog_database()
    annotation_eggnog(input_file,output_file)
