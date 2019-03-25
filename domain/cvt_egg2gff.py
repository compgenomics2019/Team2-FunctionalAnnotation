#!usr/bin/python

import sys,re

def read_reference_file(filename):
    with open(filename,'r') as f:
        for line in f:
            if re.match('>',line):
                lis = line.split()
                print(lis)

    pass

def read_eggNOG_file(filename):
    pass

def main():

    file_reference = sys.argv[1]
    file_eggNOG = sys.argv[2]

    read_reference_file(file_reference)
    read_eggNOG_file()
