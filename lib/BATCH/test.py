text_file = open("first.htm", "r")

lines = text_file.readlines()
for i in range(1000):
    myfile = open("{}.htm".zfill(2).format(i), "w")
    for line in lines:
        myfile.writelines(line.replace("{number}", str(i+1)))
    myfile.close()
text_file.close()
