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

    lis_sorted = sorted(lis, key=lambda x: int(x[0].split("_")[1]))
    lis_sorted2 = sorted(lis_sorted, key=lambda x: int(x[0].split("_")[1]))

    return lis_sorted2

def add_ids_act_nc(input_file,output_file):

    lis_nodes = readfile(input_file)
    lis_sort = sort_list(lis_nodes)
    
    f = open(output_file,"w")
    f.write("##gff-version3\n")
    for element in lis_final:
        f.write('\t'.join(element))
    
if __name__ == '__main__':
    add_ids_act(sys.argv[1],sys.argv[2])
