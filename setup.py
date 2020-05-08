
import sys
from subprocess import call,check_output

test_file = "./Downloads/Assignment2/Test.csv"
train_file = "./Downloads/Assignment2/Train.csv"
f = open(test_file,"r")
lines = f.readlines()

mapper = "mapper-knn.py"
reducer = "reducer-knn.py"
ip = "input-knn"
op = "output-knn"

for i,l in enumerate(lines):
	if i == 0: continue
	# cmd = "cat "+train_file+" | python3 mapper-knn.py "+ l.strip() + " | python3 reducer-knn.py"
	cmd = "hadoop jar /home/cse587/hadoop-3.1.2/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
	-file "+ mapper + " -mapper '"+ mapper+ " " +l.strip() + "' \
	-file "+ reducer + " -reducer "+ reducer + " \
	-input /hdworkspace/"+ ip +" -output /hdworkspace/"+ op +"/"+str(i)


	exc = call(cmd,shell=True)


if exc !=0: exit(1)

cmd = "hdfs dfs -copyToLocal /hdworkspace/"+op+ " ./Documents"
exc = call(cmd,shell=True)
if exc != 0: print("error")

dirs = ["./Documents/output-knn/"+str(i+1) for i in range(15)]
file_name = "/part-00000"

output_knn = "./final-knn-output.csv"
op = open(output_knn,"w+")
for d in dirs:
	path = d + file_name
	file = open(path,"r")
	lines = file.readlines()
	for l in lines:
		l = l.strip()
		if len(l) > 1:
			op.writelines(l)
op.close()