class programmer:
    company="microsoft"
    def __init__(self,name,product):
            self.name=name
            self.product=product
    def getinfo(self):
          print(f"The name of programmer is {self.name} the name of product is {self.product}")

anand=programmer("Anand","VS code")
anand.getinfo()