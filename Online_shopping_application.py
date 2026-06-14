class Online_Shopping_System:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def add_to_cart(self):
        print("Added to cart....")
    def remove_from_cart(self):
        print("Removed from cart....")
class Electronics(Online_Shopping_System):
    def __init__(self,category):
        super().__init__("Laptop","400000",category)
    def apply_warranty(self):
        print("Warranty applied....")
    def check_specs(self):
        print("Specs displayed....")
        
class Clothing(Online_Shopping_System):
    def __init__(self,category):
        super().__init__("Chudidhar","3000",category)
    def select_size(self):
        print("Size selected....")
    def try_on(self):
        print("Trying clothes....")
shopping = Electronics("Electorincs")
shopping.apply_warranty()
shopping.check_specs()
print(shopping.name,shopping.price,shopping.category,sep = "\n")
print()
shopping = Clothing("Clothing")
shopping.select_size()
shopping.try_on()
print(shopping.name,shopping.price,shopping.category,sep = "\n") 
