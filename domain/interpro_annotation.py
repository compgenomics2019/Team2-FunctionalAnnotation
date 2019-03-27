#!usr/bin/python 3

import sys,os

# Usage: interpro_annotation <input_file> <output_file>

def annotation_interproscan(input_file,output_file):
    
    # Apply all database for protein searching
    os.system("/projects/team3/func_annot/bin/interproscan/interproscan-5.33-72.0/interproscan.sh -i " + input_file + " -f gff3 -o " + output_file + " -dp")

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    annotation_interproscan(input_file,output_file)

if __name__ == '__main__':
    main()
