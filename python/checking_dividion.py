num1=int(input("Enter the number"))
if num1%15==0:
    print("number is divisiable by 15")
else:
    if num1%5==0 or num1%3==0:
        print("number is divisiable by 5 or 3 nut not by 15")
    else:
        print("number is not divisiable 5 or 3 or 15")