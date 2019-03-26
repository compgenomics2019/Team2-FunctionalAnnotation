import os

all_files = os.listdir("95/")
txt_files = filter(lambda x: x[-4:] == '.gff', all_files)
length = []
name = []
for file in txt_files:
	i = os.popen("wc -l "+"95/" +file).read()
	i = i.strip()
	i = i.split(' ')
	tmp = i[1].split('/')
	length.append(i[0])
	name.append(tmp[1])
print(length)
print(name)
chart = open('95chart.txt','w')
chart.write(','.join(name))
chart.write('\n')
chart.write(','.join(length))