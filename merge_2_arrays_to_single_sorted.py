# Merge two arrays into a single sorted array

# arr1 = [2,5,3,6]
# arr2 = [1,4,8,9]

# merged = arr1 + arr2
# merged.sort()
            
# print(merged)

arr1 = [2,5,3,6]
arr2 = [1,4,8,9]

merged = arr1 + arr2

for i in range(len(merged)):
    for j in range(len(merged) - i - 1):
        if merged[j] > merged[j + 1]:
            merged[j], merged[j + 1] = merged[j + 1], merged[j]

print(merged)
            