import streamlit as st

# Title
st.title("Price Calculator")

# Text input for name
price=st.number_input("Enter Product Price",min_value=0.0,value=0.0)

# Discount Slider from 0% to 50%
discount=st.slider("Select Discount Percentage",min_value=0,max_value=50,value=0)

# Calculate button
if st.button("Calculate Discount"):
    if price>0:
        
# Calculate discount amount
        
        discount_amount=price*discount/100
        
# Calculate Final price
        
        final_price=price-discount_amount
        
# Display result
        st.success(f"Final Price ₹{final_price:.2f}")
        
# Display other details
        st.write("Original Price : ₹",price)
        st.write("Discount : ",discount,"%")
        st.write("Discount Amount : ₹",discount_amount)
        
# Optional comparison table 
        st.write("Price Comparison")
        
        comparison=[["Before",f"{price:,.2f}"],["After",f"{final_price:,.2f}"]]
        
        st.table(comparison)
        
    else:
        st.error("Please enter a product price greater than 0")