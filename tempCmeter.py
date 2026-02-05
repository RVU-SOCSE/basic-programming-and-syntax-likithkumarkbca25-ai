t=float(input("enter temperature"))
print("1.C->F  2.F->C")
x=int(input("enter option"))
match x:
    case 1:
        temp1=(t*9/5)+32
        print("celsius to fahranheit=",temp1)
    case 2:
        temp2=(t-32)*5/9
        print("fahrenheit to celsius=",temp2)
    case _:
        print("invalid option")
      
