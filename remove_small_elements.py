# Today's Question: Remove elements smaller than a given value.
# inp: lis=[5,8,3,2,9,7] val=4
# out: [5,8,9,7]


numbers = [5,8,3,2,9,7]

value = 4

filtered_numbers = []

for x in numbers:
    if x >= value:
        filtered_numbers.append(x)

print(filtered_numbers)