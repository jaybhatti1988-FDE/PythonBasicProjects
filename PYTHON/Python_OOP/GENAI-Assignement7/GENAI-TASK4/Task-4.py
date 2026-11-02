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

    def get_info(self):
        print("Product Name :",self.name)
        print("Price : ₹",self.__price)
        print("Category : ",self.category)

# Laptop Class
class Laptop(Product):
    
# Override get_info()
    def get_info(self):
        print("----- Laptop Details -----")
        print("Laptop Name :",self.name)
        print("Laptop Price : ₹",self.get_price())
        print("Category : ",self.category)
    
# Mobile Class
class Mobile(Product):
    
# Override get_info()
    def get_info(self):
        print("----- Mobile Details -----")
        print("Mobile Name :",self.name)
        print("Mobile Price : ₹",self.get_price())
        print("Category : ",self.category)

# Create objects
laptop1=Laptop("Dell Inspiron",60000,"Laptop")
mobile1=Mobile("Samsung Galaxy",35000,"Mobile")

# Store objects in a List
products=[laptop1,mobile1]

# Demonstrate polymorphism
for product in products:
    product.get_info()
    print()