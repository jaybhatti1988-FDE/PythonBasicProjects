class Product:
    
# constructor
    def __init__(self,name,price,category):
        self.name=name
        self.__price=price # private attribute
        self.category=category

# Getter Method 
    def get_price(self):
        return self.__price

# Getter Method 
    def set_price(self,new_price):
        if new_price>0:
            self.__price=new_price
            print("Price Updated Successfully.")
        else:
            print("Invalid Price. Price must be greater than 0.")

    
# Product Information method display

    def get_info(self):
        print("Product Name :",self.name)
        print("Price : ₹",self.__price)
        print("Category : ",self.category)

# Create 1 st object
product1=Product("Laptop",60000,"Computers")

# Original Product information Display
print("Original Product Details:")
product1.get_info()

# Get price using getter
print("\nCurrent Price : ₹",product1.get_price())

# Update price using setter
product1.set_price(55000)

# Display update price
print("Updated Price : ₹ ",product1.get_price())

# Try to set an Invalid price
print("\nTrying invalid Price:")
product1.set_price(-5000)

# check price after invalid update
print("Current Price ₹",product1.get_price())