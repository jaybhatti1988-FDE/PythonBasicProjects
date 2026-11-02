class Product:
    
# constructor
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category

# Product information Method display 
    def get_info(self):
        print("Product Name :",self.name)
        print("Price :",self.price)
        print("Category : ",self.category)

# Calculate Discount Price method

    def apply_discount(self,percent):
        discount=self.price * percent/100
        discounted_price=self.price-discount
        return discounted_price

# Create 1 st object
product1=Product("Laptop",60000,"Computers")

# Create 2nd object
product2=Product("Smartphone",30000,"Mobiles")

# display product displays

print("Product 1 Details :")
product1.get_info()

print("\nProduct 2 Details :")
product2.get_info()

# Apply Discount
print("\nPrice after 10% discount on Laptop : ₹",product1.apply_discount(10))
print("Price after 20% discount on Smartphones : ₹",product2.apply_discount(20))