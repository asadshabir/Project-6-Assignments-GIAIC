'''
18. Property Decorators: @property, @setter, and @deleter
Assignment:
Create a class Product with a private attribute __price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.
'''

class Product:
    def __init__(self,price):
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,new_price):
        if new_price <0 :
            raise ValueError("Can Not Select Nagative Number ")
        self.__price = new_price
    
    @price.deleter
    def price(self):
        del self.__price
    
pp = Product(200)
print(pp.price)
pp.price = 400
print(pp.price)
del pp.price
try :
    print(pp.price)
except AttributeError :
    print("The Price Has Been Deleted!")