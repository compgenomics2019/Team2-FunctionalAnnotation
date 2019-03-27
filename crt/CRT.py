#!/usr/bin/env python3

def crt_act(input_dir):
    # Use aseemblied_genomes
    import sys
    import subprocess
    from os import listdir
    from os.path import isfile, join

    inputDir = input_dir
    print(inputDir)
    inputfiles = [f for f in listdir(inputDir) if isfile(join(inputDir, f))]
    print(inputfiles)
    for file1 in inputfiles:
        if "fasta" in file1:
            ofile = file1.split(".")[0]+"_crt.out"
            file1 = input_dir  + file1
            subprocess.call(['java', '-cp', '/projects/team2/func_annotation/bin/crt/CRISPRleader/bin/CRT1.2-CLI.jar', 'crt', file1, ofile])
