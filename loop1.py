num=int(input("enter the num"))
i=1
while i<=num:
    j=1
    while j<=num-i:
        print(" ",end="")
        j+=1
    a=1
    while a<=i:
        print("*",end=" ")
        a+=1
    i+=2
    print()
    