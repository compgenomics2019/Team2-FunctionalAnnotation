import sys,os,re

def readfile(filename):
    list_temp = []
    with open(filename,'r') as f:
        for line in f:
            if not re.match('##',line):
                list_temp.append(line.split('\t'))
    return list_temp

def pipe2one(lis):

    list_sorted = sorted(lis, key=lambda x: x[3])
    list_sorted2 = sorted(list_sorted, key=lambda x: x[0] + x[1])
    
    dic_nodes = {}

    for element in list_sorted2:
        dic_nodes[element[0]] = []
    for element in list_sorted2:       
        dic_nodes[element[0]].append(element)

    for key,value in dic_nodes.items():

        dic_nodes[key] = [key,"interproscan","protein_match",".",".",".",element[6],".","ID=;"]
        for element in value:

            if re.search("Name",element[8]):
                marker_NameA = re.search("Name",element[8]).start()
                marker_NameB = re.search(";",element[8][marker_NameA:]).start()
                Name = element[1] + "_" + element[8][marker_NameA:marker_NameA+marker_NameB+1]
            else:
                marker_NameA = 0
                marker_NameB = 0
                Name = ''

            if re.search("InterPro",element[8]):               
                marker_InterproA = re.search("InterPro",element[8]).start()
                marker_InterproB = re.search("\"",element[8][marker_InterproA:]).start()
                Interpro =  element[1] + "_" + element[8][marker_InterproA:marker_InterproA+marker_InterproB] + ";"
            else:
                marker_InterproA = 0
                marker_InterproB = 0
                Interpro = ''

            if re.search("signature_desc",element[8]):
                marker_signatureA = re.search("signature_desc",element[8]).start()
                marker_signatureB = re.search(";",element[8][marker_signatureA:]).start()
                signature = element[1] + "_" + element[8][marker_signatureA:marker_signatureA+marker_signatureB+1]
            else:
                marker_signatureA = 0
                marker_signatureB = 0
                signature = ''

            dic_nodes[key][8] = dic_nodes[key][8] + Name + Interpro + signature 
    
    return dic_nodes


def merge_one_line(input_file,output_file):

    list_ori = readfile(input_file)
    dic_output = pipe2one(list_ori)

    f = open(output_file,"w")
    f.write("##gff-version3\n")
    for key in dic_output:
        f.write('\t'.join(dic_output[key]))
        f.write("\n")
    f.close()

if __name__ == '__main__':
    merge_one_line(sys.argv[1],sys.argv[2])
