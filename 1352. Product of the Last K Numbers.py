class ProductOfNumbers:

    def __init__(self):
        self.num_l=[]
        self.product_l=[1]
        
        

    def add(self, num: int) -> None:
        if num == 0:
            self.product_l=[1]
        else:
            self.product_l.append(self.product_l[-1] * num)
        self.num_l.append(num)
        
        

    def getProduct(self, k: int) -> int:
        ind = len(self.product_l)-k-1
        if ind>=0 and ind < len(self.product_l):
            return self.product_l[-1]//self.product_l[ind]
        else:
            return 0



        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)