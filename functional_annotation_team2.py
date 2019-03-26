#!/usr/bin/env python3

import sys
import os
import re
import subprocess
import argparse
from domain import cvt_egg2gff,eggNOG_annotataion,interpro_annotation,interpro_post_acts,annotation_one_line

def main():
    parser = argparse.ArgumentParser(description='Functional annotation')
    parser.add_argument('-c', '--cluster',  help='Use the cluster file as inputs (.fasta)', type=str, required=True)
    parser.add_argument('-e', '--eggnog', help='Search against eggnog', default=False)
    parser.add_argument('-m', '--mapping', help='Mapping back to each sample', type=str)
    parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')
    args = parser.parse_args()
	
    if args.verbose:
        print("Interproscan is running for domain analysis")
    output_for_interproscan = args.cluster + '_interpro.gff'
    output_for_final = args.cluster + '_interpro_trimmed.gff'
    annotation_interproscan(args.cluster,output_for_interproscan)
    interproscan_modify(args.cluster,output_for_interproscan,output_for_final)

    if args.eggnog:
        if args.verbose:
            print("eggnog is running for domain analysis")
        output_for_eggnog = args.cluster + '_eggnog.gff'
        eggnog_act(args.cluster,output_for_eggnog)
        covert_eggnog(args.cluster,output_for_eggnog)


if __name__ == "__main__":
	main()
