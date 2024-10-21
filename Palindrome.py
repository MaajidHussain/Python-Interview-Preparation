def func(num):
    num_str=str(num)
    rev_str=num_str[::-1]
    return num_str==rev_str
    
Number=int(input("Enter a number: "))
if func(Number):
    print(True)
else:
    print(False)