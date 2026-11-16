numbers = [3,4,5,3,4,5,6,7,9,0,8]

duplicates = []

for i in range(len(numbers)):
    for j in range(i + 1 ,len(numbers)):

        if numbers[i] == numbers[j]:
            if numbers[i] not in duplicates:
                duplicates.append(numbers[i])

print(duplicates)