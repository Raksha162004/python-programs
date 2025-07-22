a=int(input("enter number of blocks:"))
b=int(input("enter number of rows:"))
c=int(input("enter number of stars:"))
sum=0
for i in range(a):
    print(f"---------BLOCK{i+1}-------------")
    count=0
    for j in range(b-i):
        for k in range(c):
            print("*",end=" ")
            count=count+1
        print()
    print(count)
    sum+=count
print(f"Total:{sum}")