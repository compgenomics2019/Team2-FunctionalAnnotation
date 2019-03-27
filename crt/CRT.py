#!/usr/bin/env python3

def crt_act(input_dir):
  import sys
  import subprocess
  from os import listdir
  from os.path import isfile, join

  inputDir = input_dir

  inputfiles = [f for f in listdir(inputDir) if isfile(join(inputDir, f))]
  for file1 in inputfiles:
    if "fasta" in file1:
      ofile = file1.split(".")[0]+"_crt.out"
      #print(ofile)
      subprocess.call(['java', '-cp', '../bin/CRT1.2-CLI.jar', 'crt', file1, ofile])
#print(inputfiles)
