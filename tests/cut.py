file = open("C:\\Users\\LeonIS\\Desktop\\temp.txt")
file1 = open("C:\\Users\\LeonIS\\Desktop\\temp1.txt","w")
for line in file:
    if line.strip() == "":
        continue
    else:
        file1.write(line)