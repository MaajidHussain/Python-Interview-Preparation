def Reverse_String(string):
    return string[::-1]
string="Hello, World"
reverse=Reverse_String(string)
print(reverse)

# 2nd Approach..

def reverse_string(string):
    rev_str=""
    for char in string:
        rev_str=char+rev_str
    return rev_str
string="Hello, World"
reversed_str=reverse_string(string)
print(reversed_str)