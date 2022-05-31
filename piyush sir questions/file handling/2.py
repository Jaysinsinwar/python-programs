#write the number from 50 to 500 in txt file in new line
f=open('2.txt','w')
for i in range(50,501):
    f.write(str(i)+"\n")
f.close()