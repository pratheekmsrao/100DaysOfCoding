print("Hello World")

def add(a,b):
    return a+b

c=add(3,3.0)
print ("c-->"+str(c))

def sub(a,b):
    return a-b

d=sub(c,3)

print("d-->"+str(d))

flie=open("day3.txt",'r')

for i in flie:
    print(i)

flie.close
fl=open("Day3.txt",'w')
fl.write("written using python")
fl.write("\n1. python functions")

fl.write("\n2. reading writing from text file")

fl.write("\n3. operators")
#fl.write("written using python")
flie.close
print("end day3")