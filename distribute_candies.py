
def distributeCandies(candyType):
    n = len(candyType)
    unique = set(candyType)
    return min(len(unique), n // 2)


candyType = [1, 1, 2, 2, 3, 3]

result = distributeCandies(candyType)

print(result)
