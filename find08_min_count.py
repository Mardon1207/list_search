def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i=0
    j=0
    n=len(data)
    m=data[0]
    s=0
    while i<n:
        if data[i]<m:
            m=data[i]
        i+=1
    while j<n:
        if data[j]==m:
            s+=1
        j+=1
    return s
data=[12,2,12,4,0,5,12,9,0]
print(find_min_count(data))
