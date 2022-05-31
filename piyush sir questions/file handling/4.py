#copy the content of the one file into another file
f1=open('1.txt','r+')
f2=open('4.txt','w')
a=f1.readlines()
for i in range(len(a)):
    f2.write(a[i])
f1.close()
f2.close()
