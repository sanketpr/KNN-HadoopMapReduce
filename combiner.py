
dirs = ["./Documents/output-knn/"+str(i+1) for i in range(15)]
file_name = "/part-00000"
for d in dirs:
	path = d + file_name
	file = open(path,"r")
	lines = file.readlines()
	for l in lines:
		l = l.strip()
		if len(l) > 1:
			print(l)