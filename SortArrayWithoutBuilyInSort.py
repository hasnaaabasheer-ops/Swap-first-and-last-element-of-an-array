arr = [4,9,6,1,2,0,1,4,5,3]

for i in range(len(arr)):
    for j in range(i + 1,(len(arr))):
        if arr[i] > arr[j]:
            temp = arr[j]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)