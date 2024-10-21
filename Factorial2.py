def Factorial(Number):
    if Number<0:
        return 0
    elif Number==0 or Number==1:
        return 1
    else:
        Fact=1
        while(Number>1):
            Fact=Fact*Number
            Number=Number-1
        return Fact
Number=int(input("Enter any whole number: "))
print("Factorial of",Number,"is",Factorial(Number))
