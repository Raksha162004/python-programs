num=int(input("enter any number:"))
def gcd(a,b):
    while(b!=0):
        temp=a%b
        a=b
        b=temp
    return a

def cop(a,b):
    return gcd(a,b)==1



for i in range(1,num):
    for j in range(1,i):
        for k in range(1,j):
            if(k*k+j*j==i*i and cop(i,j) and cop(j,k) and cop(k,i)):
                print(k,j,i)
