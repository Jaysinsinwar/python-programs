f=open('5a.txt','r')
f2=open('5.txt','w')
lines=f.readlines()
for i in lines:
    x=i.split(".")
    if(x[0]=='172'):
        f2.write(i)
f.close()
f2.close()