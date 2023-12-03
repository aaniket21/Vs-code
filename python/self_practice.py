# #
# list_length= int(input("Enter length of list: "))
# while list_length>5:
#     n=(int(input("Enter number: ")))
#     List1=list.append(n)
# print(List1)

# #sum of two given number using def function
# def sum(n1,n2):
#     ans = n1+n2
#     return ans

# x=int(input("Num1: "))
# y=int(input("Num2: "))
# ans = sum(x,y)
# print(ans)

# # loop practice using if-else statement
# yos=int(input("Year of service: "))
# salary=int(input("Enter your current salary: "))

# if yos>5:
#     print("Bonus is ",salary*0.05)
# else:
#     print("Not eligiable for Bonus")


# length=int(input("Enter the length: "))
# breadth=int(input("Enter the breath:"))

# if length==breadth:
#     print("It is a square")
# else:
#     print("It is a rectangle")

# #loop practice
# num1=int(input("Num1: "))
# num2=int(input("Num2: "))

# if num1>num2:
#     print("Num1 is greatest ")
# else:
#     print("Num2 is greatest")

# quantity=int(input("No. of products to buy: "))
# cost=100*quantity
# if quantity>1000:
#     print("Total cost is",cost-(cost*0.1))
# else:
#     print("Total cost is",cost)

# num=int(input("Enter number: "))

# if num<0:
#     print("The number is",-num)
# else:
#     print("The number is",num)

# fibonachi series:-

# int1= int(input("Num: "))
# L=[]
# def fibo(n):
#     if (n==0):
#         return 0
#     elif (n==1):
#         return 1
#     else:
#         L.append(fibo(n-1) + fibo(n-2))
#       #
# fibo(int1)
# for i in L:
#     print(i)

# taking input from user and removing first letter from both string and concatinating both string :-
# str1=input("str1:")
# str2=input("str2:")
# str3=str1[1:]+str2[1:]
# L1=len(str1)
# L2=len(str2)
# if L1<=1 and L2<=1:
#     print("null")
# else:
#     print("str3: ",str3)


# taking input from user and converting into list without '' in list:-

# input_str=input("enter no. with space: ")
# List=input_str.split(" ")
# print("List: ",List)


# slicing of srting:-
# a="LIBRARY"
# print("output: ",a[-7:-2:-1])


# Write a programm to which will add a stream of numbers inputed by user. the adding stop as soon as user enter "q" key on keyword:-

# sum = 0
# while True:
#     num=input("Enter the price of product: ")
#     if num=="q":
#         print("Total amount:",sum)
#         break
#     else:
#         num1=int(num)
#         sum=sum+num1

#  Write a Python function to find the maximum of three numbers. :-

# def max(m,n,o):
#     if m>n and m>o:
#         return m
#     elif n>m and n>o:
#         return n
#     else:
#         return o

# num=int(input("Enter the first char: "))
# num2=int(input("Enter the second char: "))
# num3=int(input("Enter the third char: "))
# print("Max no. is ",max(num,num2,num3))

# Write a Python function to sum all the numbers in a list.
# def list_sum(number):
#     sum=0
#     for i in number:
#         # a=int(i)
#         sum=sum+i
    
#     return sum

# num=int(input("Enter the length of list: "))
# L=[]
# for i in range(0,num+1):
#     data=int(input("Enter the list no.: "))
#     L.append(data)
# print("Sum of list is: ",list_sum(L))





# str=input("Enter the word: ")
# dup=[]
# for i in str:
#     if i not in dup:
#         dup.append(i)
#     else:
#         print("duplicate char: ",i)

str=input("Enter your string: ")
vowel=["a","e","o","u","i","A","E","I","O","U"]
s=""
s1=""
for i in str:
    if i in vowel:
        s=s+i
    else:
        s1=s1+i
s2=s1[::-1]
print(s+s2)