def anagram(a,b):
    if(sorted(a)==sorted(b)):
        return(True)
    else:
        return(False)



(a,b)=map(str,input("Enter two string separated with space").split())
x=anagram(a,b)
if(x):
    print("anagram")
else:
    print("NOt anagram")
