def Biggest_Element(List):
    large=List[0]
    for i in range(1,len(List)):
        if List[i] > large:
            large=List[i]
    return large
List=[20,25,32,15,30]
print("The biggest element in the given list is",Biggest_Element(List))
