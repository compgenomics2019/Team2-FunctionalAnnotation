#!/usr/bin/env python3

import sys
import subprocess
from os import listdr
from os.path import isfile, join

inputDir = sys.argv[1]

inputfiles = [f for f in listdir(inputDir) if isfile(join(inputDir, f))]
for file1 in inputfiles:
  if "fasta" in file1:
    ofile = file1.split(".")[0]+"_crt.out"
    #print(ofile)
    subprocess.call(['java', '-cp', 'CRT1.2-CLI.jar', 'crt', file1, ofile])
#print(inputfiles)
