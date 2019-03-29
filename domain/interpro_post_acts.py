#!usr/bin/python 3
import sys,re,os 

def read_reference(filename):
    dic_reference = {}
    with open(filename,'r') as f:
        for line in f:
            if re.match('>',line):
                dic_reference[line.split()[0][1:]] = [line.split()[2],line.split()[4]]
    f.close()

    return dic_reference

def read_origff(filename,dic_reference):
    list_replace_sites = []
    with open(filename,'r') as f:
        for line in f:
            if not re.match('##',line):
                if line.split()[0] in dic_reference:
                    newline = line.split('\t')
                    newline[3] = str(int(line.split('\t')[3]) + int(dic_reference[line.split('\t')[0]][0]))
                    newline[4] = str(int(line.split('\t')[4]) + int(dic_reference[line.split('\t')[0]][1]))
                    list_replace_sites.append(newline)
    f.close()
    return list_replace_sites
            
def trim_list(list_to_be_trimemd):
    list_trim = []
    not_contain = []
    for i in range(1,len(list_to_be_trimemd)-1):
        if list_to_be_trimemd[i] not in list_trim and list_to_be_trimemd[i] not in not_contain and list_to_be_trimemd[i][2] != 'polypeptide':
            if list_to_be_trimemd[i][0] == list_to_be_trimemd[i+1][0] and list_to_be_trimemd[i][1] == list_to_be_trimemd[i+1][1]:
                if list_to_be_trimemd[i][3] == list_to_be_trimemd[i+1][3] and list_to_be_trimemd[i][4] == list_to_be_trimemd[i+1][4]:
                    if list_to_be_trimemd[i][5] < list_to_be_trimemd[i+1][5]:
                        list_trim.append(list_to_be_trimemd[i])
                        not_contain.append(list_to_be_trimemd[i+1])
                    else: 
                        list_trim.append(list_to_be_trimemd[i+1])
                elif int(list_to_be_trimemd[i][4]) <= int(list_to_be_trimemd[i+1][3]) :
                    list_trim.append(list_to_be_trimemd[i])
                elif int(list_to_be_trimemd[i][4]) > int(list_to_be_trimemd[i+1][3]):
                    continue
            else:
                list_trim.append(list_to_be_trimemd[i])
    return list_trim

def interproscan_modify(cluster,inputs,output):

    os.system("awk '{if($6 < 0.001) print}' " + inputs + " > " + inputs[:-4] + "_evalue.gff")
    
    # cluster is cluters file, inputs are interproscan gff file, output is gff after modification
    inputs_new = inputs[:-4] + "_evalue.gff"

    file_reference = cluster
    file_origff = inputs_new
    file_output = output

    dic_reference = read_reference(file_reference)
    list_replace_sites = read_origff(file_origff,dic_reference)

    list_replace_sites_new = sorted(list_replace_sites, key=lambda x: x[3])
    list_replace_sites_new2 = sorted(list_replace_sites_new, key=lambda x: x[0] + x[1])

    list_trimed = trim_list(list_replace_sites_new2)

    os.system("rm " + inputs_new)  

    with open(file_output,'w') as f:
        f.write("##gff-version 3\n")
        for line in list_trimed:
            f.write('\t'.join(line))
    f.close()

def main():
    interproscan_modify(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == '__main__':
    main()
