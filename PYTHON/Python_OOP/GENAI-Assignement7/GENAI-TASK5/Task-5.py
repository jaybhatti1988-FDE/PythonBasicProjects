from abc import ABC,abstractclassmethod

# Abstract Class
class Payment(ABC):
    
    @abstractclassmethod
    def process_payment(self,amount):
        pass
    
# Child class 1
class CreditCardPayment(Payment):
    
    def process_payment(self, amount):
        print("Credit Card payment of ₹",amount ,"processed Successfully. ")

# Child class 2
class UPIPayment(Payment):
    
    def process_payment(self, amount):
        print("UPI payment of ₹",amount ,"processed Successfully. ")
        
# Create Objects
credit_card=CreditCardPayment()
upi=UPIPayment()

# Test Payments Methods
credit_card.process_payment(50000)
upi.process_payment(25000)