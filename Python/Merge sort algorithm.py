arr = [4, 6, 2, 1, 3, 5]

def mergeSort(arr): 
    if len(arr) >1:
        R = arr[len(arr)//2:]
        L = arr[:len(arr)//2]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
print('Input: ' + str(arr))
mergeSort(arr)
print('Output: ' + str(arr))
