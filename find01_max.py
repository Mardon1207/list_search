def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    i=0
    n=len(data)
    m=data[0]
    while i<n:
        if data[i]>m:
            m=data[i]
        i+=1
    return m
data=[1,2,3,4,5,12,9,0]
print(find_max(data))
    