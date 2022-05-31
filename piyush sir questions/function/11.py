def panagram(s):
    a=s.lower()
    b='abcdefghijklmnopqrstuvwxyz'
    for i in b:
        if i not in a:
            return(False)

a=input("Enter string:")
c=panagram(a)
if(c==False):
    print("string is not panagram :")
else:
    print("string is panagram")

