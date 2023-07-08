arr = [4, 5, 2, 3, 4, 32] #, 23, 45, 74, 23, 13, 4, 964, 54, 45, 73, 84]

for i in range(len(arr)):
    min_valu = i
    for j in range(i+1, len(arr)):
        # Hear we need arr[min_value] to compare
        #print(arr[i])
        #print('arr[min_valu]',arr[min_valu])
        if arr[min_valu] > arr[j]:
            min_valu = j

    arr[i], arr[min_valu] = arr[min_valu], arr[i]

print(arr)