# Today's Question:Move all zeros to the end of the list without changing the order of other elements.
# Input lis = [0, 5, 0, 8, 3, 0, 7]
# Output lis [5, 8, 3, 7, 0, 0, 0]


num = [0,5,0,8,3,0,7]

result = []

for i in num:
    if i != 0:
        result.append(i)

zeros = num.count(0)
for i in range(zeros):
    result.append(0)
print(result)