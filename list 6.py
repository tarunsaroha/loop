row=int(input("enter the number"))
colum=int(input("enter the number"))
i=1
while i<=row:
    j=1
    while j<=colum:
        if i==1 or i==(row) or j==1 or j==(colum):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1