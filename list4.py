nums=[10,2,5,7,-1,-8,0]
even_nums=[]
odd_nums=[]
positive=0
negative=0
zero=0
for i in nums:
    if i%2==0:
        even_nums.append(i)
    else:
        odd_nums.append(i)
    if i>0:
        positive+=1
    elif i==0:
        zero+=1
    elif i<0:
        negative+=1
print("even numbers:",even_nums)
print("odd numbers:",odd_nums)
print("positive numbers:",positive)
print("negative numbers:",negative)
print("Zeros:",zero)



