""" mergeSort
Implement the Merge Sort algorithm to sort arrays. The input is a one-dimensional array
of integers.
"""


def mergeSort(arr):
    recurMS(0, len(arr), arr)
    return arr

def recurMS(start, end, arr):
    if end - start < 2:
        return
    mid = start + (end-start) // 2
    recurMS(start, mid, arr)
    recurMS(mid, end, arr)
    temp = []
    right = mid
    for left in range(start, mid):
        while right < end and arr[right] < arr[left]:
            temp.append(arr[right])
            right += 1
        temp.append(arr[left])
    arr[start:start+len(temp)] = temp


print(mergeSort([4, 3, 7, 2, 5, 8, 27, 0, 2, 2])) # [0, 2, 2, 2, 3, 4, 5, 7, 8, 27]
