s = open('shopping.txt')
line=s.readline()
while len(line)!=0:
    print(line, end ='')
    line=s.readline()
#for eachline in myFile:
#    print(eachline)
s.close()