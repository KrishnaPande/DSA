arr = [4, 5, 2, 3, 4, 32 , 23, 45, 74, 23, 13, 4, 964, 54, 45, 73, 84]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j = j - 1
    else:
        arr[j + 1] = key

print(arr)

# selection Sort
for i in range(len(arr)):
    min = arr[i]
    for j in range(i + 1, len(arr)):
        if arr[j] < min:
            min = arr[j]
    arr[i], min = min, arr[i]

print(arr)

# Buble Sort

for j in range(len(arr)):
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            arr[i + 1], arr[i] = arr[i], arr[i + 1]

print(arr)