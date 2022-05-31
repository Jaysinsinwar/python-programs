
f=open('6.txt','r')
lst1=[]
lst2=[]
lines=f.readlines()
for i in lines:
    
    x=i.split()
    print(i)
    
    print("hii")
    # avg1=float(x[1])
    # lst1.append(avg1)
    # avg2=float(x[2])
    # lst2.append(avg2)
print(lst1)
print(lst2)
f.close()