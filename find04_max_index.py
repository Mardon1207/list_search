def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    i=0
    s=0
    n=len(data)
    m=data[0]
    while i<n:
        if data[i]>m:
            m=data[i]
            s=i
        i+=1
    return s
data=[1,2,13,4,5,12,9,0]
print(find_max_index(data))
    
