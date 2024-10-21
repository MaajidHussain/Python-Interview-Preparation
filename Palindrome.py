def Palindrome(Input):
    Input_str=str(Input)
    rev_str=Input_str[::-1]
    return Input_str==rev_str
    
Input=input("Enter any String / Number: ")
if Palindrome(Input):
    print(True)
else:
    print(False)
