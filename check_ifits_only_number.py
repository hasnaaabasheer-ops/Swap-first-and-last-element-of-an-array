# Today's question: Check if a given list contains only numbers.

# Inp: ["7", "0", "python", "6", "sql"]
# out: False

# Inp: ["7", "5", "2", "8"]
# out: True

numbers = ["7","0","python","6","sql"]

result = True

for i in numbers:
    if not i.isdigit():
        result = False
        break

print(result)

numbers = ["7","5","2","8"]

result = all(i.isdigit() for i in numbers)

print(result)