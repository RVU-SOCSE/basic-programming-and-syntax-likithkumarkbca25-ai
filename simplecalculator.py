x=int(input("enter 1st number"))
y=int(input("enter 2nd number"))
print("1.add 2.sub 3.mul 4.div")
i=int(input("choose option"))
match i:
    case 1:
        sm=x+y
        print("sum=",sm)
    case 2:
        sb=x-y
        print("sub=",sb)
    case 3:
        ml=x*y
        print("mul=",ml)
    case 4:
        dv=x//y
        print("div=",dv)
    case _:
        print("invalid option")

    
