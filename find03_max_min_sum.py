def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    i=0
    n=len(data)
    m=data[0]
    k=data[0]
    s=0
    while i<n:
        if data[i]>m:
            m=data[i]
        if data[i]<m:
            k=data[i]
        i+=1
    return m-k
data=[12,2,12,4,5,12,9,0]
print(find_max_min_sum(data))
