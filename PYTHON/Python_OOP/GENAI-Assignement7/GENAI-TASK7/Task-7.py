# Product Class

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
            
# Display Product Information

    def get_info(self):
        print("Product Name :",self.name)
        print("Price : ₹",self.__price)
        print("Category : ",self.category)

# Magic Methods

    def __str__(self):
        return f"Product({self.name},{self.__price},{self.category})"
    
# Operator Overloading
    def __add__(self, other):
        return self.__price+other.__price

# Inventory Class
class Inventory:

    def __init__(self):
        self.products=[]
        
# Add products
    def add_product(self,product):
        self.products.append(product)
        print(product.name,"added successfully.")
        
# Remove products by name
    def remove_product(self,name):
        for product in self.products:
            if product.name==name:
                self.products.remove(product)
                print(name,"removed successfully.")
                return
            
        print(name,"not found in inventory.")
            
# Calculate total inventory value

    def get_total_value(self):
        total=0
        
        for product in self.products:
            total+=product.get_price()
        return total
    
# Display All Products
    def show_all_products(self):
        print("\n------- All Products -------")
        
        for product in self.products:
            product.get_info()
            print()

# Store Class
class Store:
    
    def __init__(self,store_name):
        self.store_name=store_name
        self.inventory=Inventory()

# Create Product Object
    def add_new_product(self):
        name=input("Enter product name :")
        price=float(input("Enter product price :"))
        category=input("Enter product category :")
        
        product=Product(name,price,category)
        
        self.inventory.add_product(product)

# Display Store Summary
    def show_summary(self):
        print("\n------- Store Summary -------")
        print("Store Name :",self.store_name)
        print("Total Items :",len(self.inventory.products))
        print("Total Inventory Value : ₹",self.inventory.get_total_value())

# Test Inventory System

# 1. Create a store object
store=Store("Electronics World")

# 2. Add 3 products
print("\n Enter First Product")
store.add_new_product()

print("\n Enter Second Product")
store.add_new_product()

print("\n Enter Third Product")
store.add_new_product()

#3 Show All Products
store.inventory.show_all_products()

#4 Show Summary
store.show_summary()

# 5 Use __add__ to combine prices of two products
product1=store.inventory.products[0]
product2=store.inventory.products[1]

combine_prices=product1+product2

print("\nCombined Prices of First Two Products : ₹",combine_prices)