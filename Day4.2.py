a=int(input("total user:"))
if(a<0):
    print("INVALID INPUT")
elif(a==0):
    print("there is no staff and student user")
else:
    b=int(input("staff user:"))
    if(b<0):
        print("INVALID INPUT")
    elif(b==0):
        print("student user =",a)
    elif(a<b):
        print("INVALID INPUT")
    elif(a==b):
        print("student user =0")
    else:
        c=a-b
        d=c-b/3
        print("student user =",int(d))
