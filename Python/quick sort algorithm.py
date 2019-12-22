# Quick sort
arr = [1, 5, 2, 4, 6, 3, 7, 9, 8]

def quick_sort(arr):
    left = []
    mid = []
    right = []

    if len(arr) > 1:
        pivot = arr[0]
        for i in arr:
            if i > pivot:
                right.append(i)
            elif i == pivot:
                mid.append(i)
            else:
                left.append(i)

        return quick_sort(left) + mid + quick_sort(right)
    else:
        return arr


print(quick_sort(arr))
