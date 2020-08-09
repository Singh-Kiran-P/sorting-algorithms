def mergeLists(l1, l2):
    i = 0
    j = 0
    res = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    res += l1[i:]
    res += l2[j:]
    return res

def mergeSort(l):
    """Merge sort algorithm implementation."""
    if len(l) <= 1:  # base case
        return l
    # divide array in half and merge sort recursively
    half = len(l) // 2
    left = mergeSort(l[:half])
    right = mergeSort(l[half:])
    return mergeLists(left, right)



