# Question: Remove elements that appear an odd number of times

a = list(map(int, input("Enter elements: ").split()))

count = {}

for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
result = [x for x in a if count[x] % 2 == 0]

print(result)