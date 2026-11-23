# Ques : Find common elements between three arrays.
# inp : first = [8,3,7,1] , second = [9,2,7,8], third = [9,7,8,2]
# out: [8,7]

ele1 = [8,3,7,1]
ele2 = [9,2,7,8]
ele3 = [9,7,8,2]

result = []

for i in ele1:
    if i in ele2 and i in ele3:
        result.append(i)
print(result)