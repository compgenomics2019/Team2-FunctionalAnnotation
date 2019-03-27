#!usr/bin/python 3

import sys 
from subprocess import Popen, PIPE

# Usage: interpro_annotation <input_file> <output_file>

def annotation_interproscan(input_file,output_file):
    
    # Apply all database for protein searching
    logfile1 = open("./logfile_interpro_stdout.log",'w')
    logfile2 = open("./logfile_interpro_stderr.log",'w')
    
    process = Popen(args = ['interproscan.sh',   
                            '-i',input_file,    
                            '-f','gff3',     # hmmer method can be replaced
                            '-o',output_file,'-dp'],
                            stdout = logfile1, stderr = logfile2)
    stdout, stderr = process.communicate()
    
    del stdout,stderr

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    annotation_interproscan(input_file,output_file)

if __name__ == '__main__':
    main()
