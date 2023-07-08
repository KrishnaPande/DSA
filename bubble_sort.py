arr = [4, 5, 2, 3, 4, 32 , 23, 45, 74, 23, 13, 4, 964, 54, 45, 73, 84]

for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)