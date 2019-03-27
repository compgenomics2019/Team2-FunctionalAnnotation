import os
import sys
import re
import copy


Allfaa_file_name = 'All_Prodigal.faa'

# Take the result from prodigal protein
def relabel(In_path, Cluster_path): #need a path to a directory for 50 fasta and specify cluster directory
    relabel_file = []
    for file in os.listdir(In_path):
        if file.endswith(".faa"):
            relabel_file .append(file)


    # Relabel the contig files and generate Relabel directory with relabel contig files
    os.mkdir('./Relabel', 0755)
    for FileName in relabel_file:
        InFile = open(In_path + '/' + FileName, 'r')
        OutFile = open('./Relabel/' + FileName, 'w')
        Label = re.split(';|\.|_|/',FileName)[-3]
        pattern = re.compile("^>")
        for line in InFile:
            if pattern.match(line):
                line = line[:1] + Label + '_' + line[1:]
            OutFile.write(line)
        InFile.close()
        OutFile.close()

# Merge the relabel file togethor and Run Uclust command line in Cluster directory
    Allfaa_path2file = Cluster_path + '/All_Prodigal.faa'
    os.mkdir(Cluster_path, 0755)
    os.system('cat ./Relabel/* > ' + Allfaa_path2file)
    Cluster_path2fastafile = Cluster_path + '/ProdigalCluster_97.fasta' 
    Cluster_path2ucfile = Cluster_path + '/ProdigalCluster_97.uc' 
    os.system('usearch -cluster_fast '+ Allfaa_path2file + ' -id 0.97 -centroids ' + Cluster_path2fastafile  + ' -uc ' + Cluster_path2ucfile)
    os.system('rm ' + Allfaa_path2file)
    return Cluster_path2fastafile, Cluster_path2ucfile



# Mapping clusters back to contig and create Func_annotation_result directory with all the gff file
def mapping_back(dirs, cluster_path, output_gff_path): 
# list of directory that contain cluster gff file, path the uc cluster file, path to final gff output directory,
    d = {}
    for file in os.listdir("./Relabel"):
        if file.endswith(".faa"):
            file = file.split('_')[0]
            d[file] = []

    for file in os.listdir(cluster_path):
        if file.endswith(".uc"):
            cluster_file = file

    f = open(cluster_path + '/' + cluster_file, 'r')
    Pos_map = {}
    cluster = {}
    for line in f:
        lines = line.strip().split('\t')
        if lines[0] == 'S':
            data = lines[8].split(' ')
            lines[8] = data[0]
            cluster[lines[8]] = []
            if lines[8] not in Pos_map:
                Pos_map[lines[8]] = (data[2], data[4], data[6])
        elif lines[0] == 'H':
            data = lines[8].split(' ')
            lines[8] = data[0]
            lines[9] = lines[9].split(' ')[0]
            cluster[lines[9]].append(lines[8])
            if lines[8] not in Pos_map:
                Pos_map[lines[8]] = (data[2], data[4], data[6])


    # dirs = ['./eggNOG', './interproscan', './operon','./vfdb','./victors']

    gff_files = []
    for dir in dirs:
        gff_files += [( dir + '/' + name) for name in os.listdir('./' + dir) if name.endswith(".gff")]

    for gff in gff_files:
        f = open(gff, 'r')
        for line in f:
            lines = line.strip().split('\t')
            contig = lines[0].split('_')[0] #CGT2006
            if contig in d:
                pos = lines[0].find('_')
                temp = copy.deepcopy(lines)
            #add this two line
                temp[3] = Pos_map[temp[0]][0]
                temp[4] = Pos_map[temp[0]][1]
            #--------------         
                temp[0] = temp[0][pos+1:]
                d[contig].append('\t'.join(temp) + '\n')
                if cluster[lines[0]]:
                    for elem in cluster[lines[0]]:
                        lines[0] = elem
                        contig = lines[0].split('_')[0] #CGT2010
                        pos = lines[0].find('_')
                        lines[3] = .
                        lines[4] = .
                        lines[6] = .
                        lines[0] = lines[0][pos+1:]
                        d[contig].append('\t'.join(lines) + '\n')
        f.close()

    # path = './Func_annotation_result'
    os.mkdir(output_gff_path, 0755)
    for key, values in sorted(d.items(), key = lambda x:x[0], reverse = False):
        filename = output_gff_path + '/' + key + '.gff'
        f = open(filename, 'w')
        f.write('##gff-version  3\n')
        for value in values:

def merge(dirs, output_gff_path): # list of directory of 50 gff file need to be merge, output gff file path
# merge ncRNA and sigIP
    # dirs = ['./Prod_RNA_Results', './signalpgff3']
    for dir in dirs:
        for file in os.listdir(dir):
            contig = file.strip().split('_')[0]
            filename = output_gff_path + '/' + contig + '.gff'
            os.system('grep -v "^#" ' + dir + '/' + file + '>>' + filename)
def main():
    Cluster_path = './Cluster'
    Cluster_path2fastafile, Cluster_path2ucfile = relabel('./Prodigal_protein', Cluster_path)

    MapBackDir = ['./eggNOG', './interproscan', './operon', './vfdb', './victors']
    Output_gff_path = './Func_annotation_result'

    mapping_back(MapBackDir, Cluster_path, Output_gff_path)
    MergeDir = ['./Prod_RNA_Results', './signalpgff3', './resfinder', './TMHMM']
    merge(MergeDir, Output_gff_path)



if __name__ == "__main__":
    main()
