def circle():
    r=int(input("enter radius:"))
    area=3.14*r*r
    print("area of circle:",area)
def square(a):
    area=a*a
    print("area of square:",area)
def triangle():
    b=int(input("enter base of triangle:"))
    h=int(input("enter height of triangle:"))
    area=0.5*b*h
    return area
def rect(a,b):
    area=a*b
    return area
while(True):
    print("1.circle\n 2.square\n 3.triangle\n 4.rectangle\n 5.end\n")
    ch=int(input("enter your choice:"))
    match ch:
        case 1:
            circle()
        case 2:
            a=int(input("enter side of square:"))
            square(a)
        case 3:
            res=triangle()
            print("area of triangle :",res)
        case 4:
            b=int(input("enter breadth of rectangle:"))
            h=int(input("enter height of rectangle:"))
            res=rect(a,b)
            print("area of rectangle:",res)
        case 5:
            exit(0)