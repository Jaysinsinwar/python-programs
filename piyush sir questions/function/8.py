def title(s):
    a=s.split()
    b=[]
    for i in a:
        a=chr(ord(i[0])-32)+i[1:]
        b.append(a)
    print(b)
    c=" ".join(b)
    print(c)

s=input("Enter the string separated with space:")
title(s)