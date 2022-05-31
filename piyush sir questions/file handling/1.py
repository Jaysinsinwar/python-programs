#write the number from 50 to 500 in txt file separated with space
f=open('1.txt','w')
for i in range(50,501):
    f.write(str(i)+" ")
f.close()