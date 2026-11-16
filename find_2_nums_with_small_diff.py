# Today's Question: Find two numbers that have the smallest absolute difference.
# inp: [4,9,6,1]
# out: [4,6]

nums = [4,9,6,1]

min_diff = 100
result = []

for i in range(len(nums)):
    for j in range(i + 1,len(nums)):
        if nums[i] > nums[j]:
            diff = nums[i] - nums[j]
        else:
            diff = nums[j] - nums[i]

        if diff < min_diff:
            min_diff = diff
            result = [nums[i],nums[j]]

print(result)