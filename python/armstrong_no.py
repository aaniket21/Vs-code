n=int(input("Enter no.: "))
a=str(n)
sum=0
b=len(a)
c=str(b)

for i in a:
    f=int(i)
    sum=sum+f**b
if(sum==n):
    print("number is armstrong")
else:
    print("number is not armstrong")