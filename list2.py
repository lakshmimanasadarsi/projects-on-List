tasks=["practice aptitude","practice python","learn DSA","start java"]
print(tasks)
for i,task in enumerate(tasks,start=1):
    print(i,task) 
completed=tasks.pop(0)
print("completed tasks:",completed)
print("remaining tasks:",tasks)
