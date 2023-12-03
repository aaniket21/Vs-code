cp=float(input("Cost price: "))
sp=float(input("Selling price: "))
if sp>cp:
    print("Seller get profit and the profit is",sp-cp)
elif sp==cp:
    print("Seller did not get any profit or loss")
else:
    print("Seller is in loss and loss amount is",cp-sp)