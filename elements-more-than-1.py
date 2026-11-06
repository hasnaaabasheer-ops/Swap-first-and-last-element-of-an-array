num = [10,7,4,8,9,4,7,7,10,1,7,1]

duplicate = []

for i in num:
    if num.count(i) > 1 and i not in duplicate:
        duplicate.append(i)

print(len(duplicate))
