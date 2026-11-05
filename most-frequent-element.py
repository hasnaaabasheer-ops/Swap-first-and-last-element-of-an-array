inp = [10,7,4,8,9,4,7,7,10,1,7,1]

max_count = 0
most_frequent = 0

for i in inp:
    count = 0

    for j in inp:
        if i == j:
            count += 1

    if count > max_count:
        max_count = count
        most_frequent = i

print(most_frequent)