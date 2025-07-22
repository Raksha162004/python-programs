n=int(input("enter any number:"))
l=[]
while(n not in l):
    l.append(n)
    n=sum([int(i) * int(i) for i in str(n)])
if(n==1):
    print("Round num")
else:
    print("not a round num")