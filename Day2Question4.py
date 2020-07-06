# Write a program which accepts a sequence of 
# comma-separated numbers from console and generate 
# a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


list1 = []

while True:
    nums = input("Enter number (Type 'stop' to end):" )
    if nums == 'stop':
        break
    else:
        list1.append(nums)

print(list1)
t = tuple(list1)
print(t)