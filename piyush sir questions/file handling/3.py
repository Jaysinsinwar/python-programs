import random
n=int(input("Enter the value of n:"))
f=open('3.txt','w')
lst=[]
for i in range(n):
    a=random.randrange(100,200,1)
    lst.append(a)
for i in lst:
    f.write(str(i)+' ')
f.close()