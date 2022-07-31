# TNX TO: https://www.youtube.com/watch?v=ywWBy6J5gz8&t=91s

import random

def generate(count):
    random.seed()

    out = []

    for i in range(count):
        out.append(random.randint(-10,10))

    return out

def testSorted(arr):
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            return False

    return True

def quickSort(arr, start, finish):
    if finish - start < 1:
        return
    
    pivot = arr[(finish + start) // 2]

    i = start
    j = finish

    while i <= j:
        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    if start < i-1:
        quickSort(arr, start, i-1)
    
    if i < finish:
        quickSort(arr, i, finish)

def qSort(arr):
    quickSort(arr, 0, len(arr)-1)
    
         
a = generate(23)
print(a)
qSort(a)
print(a)
print(testSorted(a))