def Factorial(number):
    if number<0:
        return 0
    elif number==0 or number==1:
        return 1
    else:
        fact=1
        while(number>1):
            fact=fact*number
            number=number-1
        return fact
Number=int(input("Enter any whole number: "))
print(Factorial(Number))