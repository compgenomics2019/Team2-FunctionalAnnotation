#!usr/bin/python 3

import sys,os

# Usage: eggNOG_annotation <input_file> <output_file>

def download_eggnog_database():

    # Before annotation, bactNOG database will be checked and installed

    print("Chekcing the eggnog database")
    os.system("python /projects/team2/func_annotation/tools/eggnog/eggnog_dataset/eggnog-mapper-1.0.3/download_eggnog_data.py -y bact")


def annotation_eggnog(input_file,output_file):
    
    # Using diamond for fast and accurate annotation
    print("Mapping to eggnog")
    os.system("python /projects/team2/func_annotation/tools/eggnog/eggnog_dataset/eggnog-mapper-1.0.3/emapper.py -i " + input_file + " -m diamond -o " + output_file)

def eggnog_act(intput,output):
    input_file = input
    output_file = output

    download_eggnog_database()
    annotation_eggnog(input_file,output_file)
