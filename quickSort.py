import random

def find(l, eval, p):
    res = []
    for i in l:
        if eval == "<" and i < p:
            res.append(i)

        if eval == ">" and i > p:
            res.append(i)

        if eval == "=" and i == p:
            res.append(i)
    return res


def quickSort(l):
    if len(l) == 0:
        return []
    else:
        p = l[random.randint(0, len(l)-1)]
        smaller = find(l, "<", p)
        l2 = find(l, "=", p)
        bigger = find(l, ">", p)
        l1 = quickSort(smaller)
        l3 = quickSort(bigger)
        return l1+l2+l3
