nums=[2,6,17,23,17,108,6]
unique=[]
for i in nums:
    if i not in unique:
        unique.append(i)
print("Original List:",nums)
print("Unique List:",unique)