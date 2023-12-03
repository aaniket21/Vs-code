list=[10,20,30,40,50]
temp=list[0] #creating temporary value
list[0]=list[4]
list[4]=temp
print(list)