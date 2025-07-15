a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
c=0
while(b!=0):
  c=a%b
  a=b
  b=c
print(a)