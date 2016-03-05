import random

def getranddata(num):
    a = []
    i = 0
    while i < num:
        a.append(random.randint(0, 100))
        i += 1
    return a

# O(n**2)
def bubbleSort(a):
    l = len(a) - 1
    for i in range(l):
        for j in range(i, l):
            if a[j+1] < a[j]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# O(n**2)
def insertSort(a):
    # 0-i is an ordered list
    for i in range(1, len(a)):
        j = i
        # compare from the ith number to the first number
        while j > 0 and a[j-1] > a[i]:
            j -= 1
        a.insert(j, a[i])
        a.pop(i+1)
    return a

# optimize the insert sort
def shellSort(a):
    a.sort()
    gap = len(a)/2
    while gap > 0:
        for i in range(0, gap):
            for j in (i + gap, len(a), gap):
                while j-gap > 0 and a[j] < a[j - gap]:
                    j = j - gap
                a.insert(j, a[i+gap])
                a.pop(i+gap)
        gap /= 2
    return a





