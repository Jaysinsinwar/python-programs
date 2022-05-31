def my_capitalize(a):
    b=chr(ord(a[0])-32)+a[1:]
    print(b)

a=input("Enter the string:")
my_capitalize(a)