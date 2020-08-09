import random
from mergeSort import mergeSort
from quickSort import quickSort

def createList(n):
  return [random.randint(0,n-1) for i in range(n)]

unOrderedList = createList(10)
print(unOrderedList)
print("-------------------------------------------")

print(quickSort(unOrderedList))
print(mergeSort(unOrderedList))
