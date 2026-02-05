x=int(input("enter 1st number"))
y=int(input("enter 2nd number"))
z=int(input("enter 3rd number"))
if x>=y and x>=z:
    maximum=x
elif y>=x and y>=z:
    maximum=y
else:
    maximum=z
if x<=y and x<=z:
    minimum=x
elif y<=x and y<=z:
    minimum=y
else:
    minimum=z
print("Maximum:",maximum)
print("Minimum:",minimum)
