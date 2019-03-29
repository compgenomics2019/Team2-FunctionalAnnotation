import sys
from subprocess import Popen, PIPE
import re

def readnames(file):
    with open(file,'r') as f:
        names = f.readlines()
    return names

def reverse (files):
#    print(file,"start")
    files = './Func_annotation_result/' + files
    output =  files[:-4] + '_sorted.gff'
    #output = file[14:32] + '_sorted.gff' 

    #from tm.pythontmhmmgff import tmhmm_act
    f = open(output,'w')
    process = Popen(args=['/projects/team3/func_annot/bin/bedtools2/bin/bedtools',
                            'sort',
                            '-i', files], stdout = f, stderr = PIPE)

    stdout, stderr = process.communicate()
    print(stderr)

def sort(names):
#    names = readnames(sys.argv[1]) 
    # print(rnammer_names,infernal_names,aragorn_names)
    for name in names:
        name = name.strip()
        print(name)
        # name = './combination/'+ name
