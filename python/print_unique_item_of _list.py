# printing unique list
# n=int(input("Enter the size of list"))
# L=[]
# M=[]
# for a in range(n):
#     num=int(input("Enter the the number: "))
#     L.append(num)
# print("Original list: ",L)

# for x in L:
#     if x not in M:
#         M.append(x)

# print("Unique list: ",M)


n=int(input("Enter the size of list"))
L=[]
M=[]
for a in range(n):
    num=int(input("Enter the the number: "))
    L.append(num)
print("Original list: ",L)

print()

print("Elements divisible by 2 and 3 are ")
for x in L:
    if x%2==0 and x%3==0:
        print(x,end=" ")