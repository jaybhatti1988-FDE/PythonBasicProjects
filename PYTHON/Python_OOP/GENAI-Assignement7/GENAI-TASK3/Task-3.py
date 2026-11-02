# Parent Class

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

    
# Product Information method display

    def get_info(self):
        print("Product Name :",self.name)
        print("Price : ₹",self.__price)
        print("Category : ",self.category)

# Child Class
class ElectronicProduct(Product):
    def __init__(self, name, price, category,warranty_years):
        super().__init__(name, price, category)
        
        self.warranty_years=warranty_years
        
# Override get_info()

    def get_info(self):
        print("Product Name :",self.name)
        print("Price : ₹",self.get_price())
        print("Category : ",self.category)
        print("Warranty :",self.warranty_years)
    
# Create object of child class
electronic1=ElectronicProduct("Smart TV",45000,"Electronics",2)

# Call overridden method
electronic1.get_info()