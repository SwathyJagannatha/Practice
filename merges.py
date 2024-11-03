def mergesort(arr):
    if len(arr) <= 1:
         return arr 
    
    mid = len(arr)//2

    leftarr = arr[0:mid]
    rightarr = arr[mid:]

    sortleft = mergesort(leftarr)
    sortright = mergesort(rightarr)

    return merge(sortleft,sortright)

def merge(a1,a2):
    result = []
    left = 0
    right = 0

    while left < len(a1) and right < len(a2):
        if a1[left] <= a2[right]:
            result.append(a1[left])
            left+=1
        else:
            result.append(a2[right])
            right+=1

    while left < len(a1):
        result.append(a1[left])
        left+=1

    while right < len(a2):
        result.append(a2[right])
        right+=1

    return result
    pass 

print(mergesort([38,27,43,3,9,82,10]))