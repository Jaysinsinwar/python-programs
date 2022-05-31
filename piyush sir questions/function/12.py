def sort(lst):
    a=len(lst)
    for i in range(a-1):
        if(lst[i]>lst[i+1]):
            a=1
        else:
            a=0
        return(a)

lst=list(map(int,input("Enter the list").split()))
b=sort(lst)
if(b==0):
    print("List already sorted")
else:
    print("List is not sorted:")

