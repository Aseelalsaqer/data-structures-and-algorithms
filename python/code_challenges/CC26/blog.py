def insertion_sort(arr):
    for i in range(1,len(arr)):
       j = i - 1
       current = arr[i]

       while j >= 0 and current < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1
                arr[j + 1] = current
    return arr

print(insertion_sort([8,4,23,42,16,15]))
