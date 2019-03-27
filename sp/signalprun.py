#!/usr/bin/python

import subprocess,os

def signalP_finding(path):
    outputdir='./signalp'
    #default path; remove # from following line if using the default on the server
    #path = '/projects/team2/gene_pred/Prodigal_results/proteins'
    Files = [f for f in os.listdir(path) if f.endswith('.faa')]
    for File in Files:
        print(File)
        Filetemp=path+'/'+File
        #print(Filetemp)
        subprocess.Popen(['/projects/team2/func_annotation/tools/signalp-5.0/bin/signalp','-fasta', Filetemp, '-org','gram-','-format','short','-gff3']).communicate()
    subprocess.call(['mkdir',outputdir])
    gff3Files = [f for f in os.listdir('./') if f.endswith('.gff3')]
    signalp5Files= [f for f in os.listdir('./') if f.endswith('.signalp5')]
    gff3Files=gff3Files+signalp5Files
    for file1 in gff3Files:
            Filetemp1='./'+file1
            subprocess.Popen(['mv',Filetemp1,outputdir]).communicate()
