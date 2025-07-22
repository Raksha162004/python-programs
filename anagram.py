str1=input("enter string 1:")
str2=input("enter string 2:")
a=str1.lower()
b=str2.lower()
a1="".join(i for i in a if i!=" ")
b1="".join(i for i in b if i!=" ")
a2=sorted(a1)
b2=sorted(b1)
if(a2==b2):
    print("it is an anagram")
else:
    print("not an anagram")