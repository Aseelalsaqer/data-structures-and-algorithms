## Pseudo Code

ALGORITHM Mergesort(arr)
DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
DECLARE i <-- 0
DECLARE j <-- 0
DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

## Code:

def mergeSort(arr):
if len(arr) > 1:
mid = len(arr)//2
L = arr[:mid]
R = arr[mid:]
mergeSort(L)
mergeSort(R)
Merge(L, R, arr)
return arr
def Merge(L, R, arr):
i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

## Trace:

[8,4,23,42,16,15]
pass 1 :
our code will start checking if len(arr) > 1 , it's true , it will find the mid point and then split the array to left [8,4,23] and
right [42,16,15] .
pass 2 :
it will do the same for the left array , len(arr) > 1 , true so it will find the mid point and then split the array to left [8] and right [4,23].
pass 3 it will check for the third left that we have if len(arr) > 1 , false , it will go to the right [4,23] will check len(arr) > 1 , true so it will split it , left [4] , right[23], now len(arr) > 1 is false for all arrays that we have .
pass 4 :
it will go to the first right [42,16,15] and keep recurrion until we have left [42] , left[16] , right[15].
pass 5 :
it will go to the next function and satrt taking the values of left an right an the array that we have merge(16,15 , []) , values of i , j , k = 0 , it will check if i < len(L) and j < len(R) , it's true so it will check the other condition L[i] < R[j] , it's fales so it will go to the else statment , arr[k] = R[j] , it will change the value of the first index of of the array [15] , increse j = 1 , k = 1 , then it will check
j < len(R) , false , then it will check i < len(L) , it's ture , it will add to the array arr[1] = 16 , [15,16] , then increase i = 1 , k = 2 .
it will keep merging every left and right until we have the full sorted array [4,8,15,16,23,42]
