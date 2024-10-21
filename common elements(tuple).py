def commonElements(List1,List2):
    #Using set() to Avoid Occuring Duplicates..
    common_elements=list(set(List1) & set(List2))
    
    return common_elements
List1= [1, 2, 3, 4, 4, 5, 5]
List2= [4, 5, 6, 7, 4, 5, 8]
common=commonElements(List1,List2)
print("Common Elements in given two lists are:",common)
