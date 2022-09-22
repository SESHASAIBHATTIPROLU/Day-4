a=input("enter the month")
b=int(input("enter the date"))
if(b>0):
    if(a=='Mar' or a=='Apr' or a=='May'):
        if (b>=20):
            print("the season is currently summer")
        else:
            print("the season is currently winter")
    elif(a=='Jun' or a=='Jul' or a=='Aug'):
        if(b>=21):
            print("the season is currently spring")
        else:
            print("the season is currently summer")
    elif(a=='Sep' or a=='Oct' or a=='Nov'):
        if(b>=22):
            print("the season is currently fall")
        else:
            print("the season is currently spring")
    elif(a=='Dec' or a=='Jan' or a=='Feb'):
        if(b>=21):
            print("the season is currently winter")
        else:
            print("the season is currently fall")
    else:
        print("enter valid three letters of month")
else:
    print("the given date is invalid")
