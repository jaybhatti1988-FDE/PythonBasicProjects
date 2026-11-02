class Product:
    
    def __init__(self,name,price,category):
        self.name=name
        self.__price=price 
        self.category=category

# Getter 
    def get_price(self):
        return self.__price

# Setter 
    def set_price(self,new_price):
        if new_price>0:
            self.__price=new_price
        else:
            print("Price must be greater than 0.")

# Magic Methods for readable String

    def __str__(self):
        return f"Product({self.name},{self.__price},{self.category})"
    
# Operator Overloading
    def __add__(self, other):
        return self.__price+other.__price

# Create 2 objects objects
product1=Product("Laptop",60000,"Computers")
product2=Product("Mobile",30000,"Mobiles")


# Test __str__()
print(product1)
print(product2)

# Test __add__()
total_price=product1+product2

print("Total Combined Price: ₹",total_price)