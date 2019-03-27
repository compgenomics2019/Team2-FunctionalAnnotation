import sys 
from subprocess import Popen, PIPE
import re

def readnames(file):
    with open(file,'r') as f:
        names = f.readlines()
    return names

def reverse (file):
    print(file,"start")
    output = file[14:32] + '_sorted.gff' 
    f = open(output,'w')
    process = Popen(args=['bedtools', 
                            'sort', 
                            '-i', file], stdout = f, stderr = PIPE)

    stdout, stderr = process.communicate()
    print(stderr)

def main():
    names = readnames(sys.argv[1]) 
    # print(rnammer_names,infernal_names,aragorn_names)
    for name in names:
        name = name.strip()
        # name = './combination/'+ name

        reverse(name)

if __name__ == '__main__':
    main()
