FileName = ("path\poem.txt")
data=file(FileName).readlines()
data.sort()
for i in range(len(data)):
    print data[i]