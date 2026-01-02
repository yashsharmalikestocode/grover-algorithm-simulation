import numpy as np


def counting_sort(arr):
    n = len(arr)
    maxx = max(arr)
    counter = [0] * (maxx + 1)
    for x in arr:
        counter[x] += 1
    i = 0
    for c in range(0, maxx + 1):
        while counter[c] > 0:
            arr[i] = c
            i += 1
            counter[c] -= 1
    return arr


def linear_search(arr, t):
    n = len(arr)
    for i in range(n):
        if arr[i] == t:
            return i
    return -1


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1


def jump_search(arr, target):
    n = len(arr) - 1
    step = int(np.sqrt(n))
    prev = 0

    if arr[step] == target:
        return step
    
    while prev < n and arr[min(step, n)] < target:
        prev = step
        step += int(np.sqrt(n))
        if arr[min(step, n)] == target:
            return step
        elif prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
        

def interpolation_search(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    pos = int(low + ((target - arr[low])/(arr[high] - arr[low])) * (high - low))
    if arr[pos] == target:
        return pos
    elif arr[pos] > target:
        L = arr[0:pos]
        low = 0
        high = pos
        interpolation_search(L, target)
    else:
        R = arr[pos:n-1]
        low = pos
        high = n-1
        interpolation_search(R, target)


def exponential_search(arr, target):
    n = len(arr)
    i = 1
    if arr[0] == target:
        return 0

    while i < n and arr[i] <= target:
        i *= 2
    
    return binary_search(arr, i // 2, min(i, n), target)

