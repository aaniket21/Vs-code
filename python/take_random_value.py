import random as r
n=r.randint(1,6)
c=1
while n!=6:
    n=r.randint(1,6)
    c=c+1
    print("Dice Throws ",c,"times to get 6")