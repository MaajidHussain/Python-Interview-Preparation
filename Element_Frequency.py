def Element_Frequency(Numbers):
    frequency={}
    for num in Numbers:
        if num in frequency:
            frequency[num]+=1
        else:
            frequency[num]=1
    return frequency
Numbers=[12,15,21,12,47,65,21,12,47]
print(Element_Frequency(Numbers))