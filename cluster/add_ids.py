import sys,re,os

def readfile(filename):
    lis_tmp = []
    with open(filename,'r') as f:
        for line in f:
            if not re.match("##",line):
                lis_tmp.append(line.split("\t"))
    f.close()

    return lis_tmp

def sort_list(lis):

    lis_sorted = sorted(lis, key=lambda x: int(x[0].split("_")[-1]))
    lis_sorted2 = sorted(lis_sorted, key=lambda x: int(x[0].split("_")[1]))

    return lis_sorted2

def add_ids(lis):
    dic_nodes = {}
    lis_tmp = []
    counter = 0
    for element in lis:
        if element[0] not in dic_nodes:
            counter = counter + 1
            dic_nodes[element[0]] = counter

    ID_prefix = "team2_fa_"
    for element in lis:
        if re.search("ID=",element[8]):
            ID_start = re.search("ID=",element[8]).start()
            ID_stop = re.search(";",element[8][ID_start:]).start()
            string_to_be_replaced = element[8][ID_start:ID_stop]
            new_string = element[8].replace(string_to_be_replaced,"ID=" + ID_prefix + str(dic_nodes[element[0]]))
            lis_tmp.append(element[:8] + [new_string])
        else:
            new_string = "ID=" + ID_prefix + str(dic_nodes[element[0]]) + ";" + element[8]
            lis_tmp.append(element[:8] + [new_string])

    return lis_tmp


def add_ids_act(input_file,output_file):

    lis_nodes = readfile(input_file)
    lis_sort = sort_list(lis_nodes)
    lis_final = add_ids(lis_sort)
    
    f = open(output_file,"w")
    f.write("##gff-version3\n")
    for element in lis_final:
        f.write('\t'.join(element))
    
if __name__ == '__main__':
    add_ids_act(sys.argv[1],sys.argv[2])
