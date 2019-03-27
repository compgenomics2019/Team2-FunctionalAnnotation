#!/usr/bin/python 3

import sys,os

# Usage: eggNOG_annotation <input_file> <output_file>

def download_eggnog_database():

    # Before annotation, bactNOG database will be checked and installed
    os.system("python /projects/team2/func_annotation/tools/eggnog/eggnog_dataset/eggnog-mapper-1.0.3/download_eggnog_data.py -y bact")


def annotation_eggnog(input_file,output_file):

    # Using diamond for fast and accurate annotation
    os.system("python /projects/team2/func_annotation/tools/eggnog/eggnog_dataset/eggnog-mapper-1.0.3/emapper.py -i " + str(input_file) + " -m diamond -d /projects/team2/func_annotation/tools/eggnog/eggnog_dataset/eggnog-mapper-1.0.3/db -o " + str(output_file))

def eggnog_act(input_file,output_file):

    download_eggnog_database()
    annotation_eggnog(input_file,output_file)
