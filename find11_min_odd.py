def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    i=0
    s=0
    n=len(data)
    m=data[0]
    while i<n:
        if data[i]<m and data[i]%2==1:
            m=data[i]
        i+=1
    return m
data=[1,2,13,4,5,12,9,0]
print(find_min_odd(data))

