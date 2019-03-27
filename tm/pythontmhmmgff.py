#!usr/bin/python 3

import sys,re,os

def read_tmhmm_output(filename):
    #count=0
    list_reference = []
    with open(filename,'r') as f:
        for line in f:
            list_temp = [None,None,None,None,None,None,None,None,None]            
            list_temp[0] = line.split()[0]
            list_temp[1] = 'TMHMM v2.0'
            list_temp[2] = 'Transmembrane Helices'
            x=''
            x= re.findall(pattern="([0-9]*)-([0-9]*)", string=line)
            #print(x)
            #print(len(x))
            y=0
            y= re.findall(pattern="PredHel=([0-9]*)", string=line)
            #print(y)
            z=y[0]
            z=int(z)
            #print(z)
            for i in range(0,z):
                list_temp = [None,None,None,None,None,None,None,None,None]            
                list_temp[0] = line.split()[0][1:]
                list_temp[1] = 'TMHMM v2.0'
                list_temp[2] = 'Transmembrane Helices'
                list_temp[3] = x[i][0]
                #print(x)
                #print(x[i][0])
                list_temp[4] = x[i][1]
                #print(x[i][1])
                #print(list_temp)
                list_temp[5] = '.'
                list_temp[6] = '.'
                list_temp[7] = '.'
                list_temp[8] = '.'
                list_temp[8] = line.split()[-1]
                #print(list_temp)
                list_reference.append(list_temp)
                #print(list_reference)
            #count = count +1
    #print(list_reference)
    return list_reference

def tmhmm_act():
    inputfiles=[]
    directory1 = "./"
    for files1 in os.listdir(directory1):
        if files1.endswith(".tmhmm"):
            inputfiles.append(files1)
        else:
            continue

    #   inputDir= sys.argv[1]
    filename1 = "/home/priyam/bin/trimtmhmm/3.tmhmm"
    start=''
    end=''

    read_tmhmm_output(filename1)
    for files in inputfiles:
            op1 = read_tmhmm_output(directory1+files)
            out_file=files.split(".")[0]+'.gff'
            #print(op1)
            #print(out_file)
            with open(out_file,'w') as of:
                #print("writing into the file")
                #fh.write("op1")
                #print(listers,file=fh)
                #print(listers)
                for line in op1:
                    of.write('\t'.join(map(str,line)))
                    of.write('\n') 
            #print(out_file)
            #print(op1,file=out_file)

