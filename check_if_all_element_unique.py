# Question: Check if all elements are unique.

# inp : [4,8,2,9,2,9]
# out : False

# inp : [3,4,1,8]
# out : True


arr1 = [4,8,2,9,2,9]
arr2 = [3,4,1,8]

for arr in [arr1,arr2]:
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                print(False)
                break
        else:
            continue
        break
    else:
        print(True)
