import streamlit as st

# Title
st.title("Product Form")

# Sidebar heading
st.sidebar.header("Add Product")

# Product name input
product_name=st.sidebar.text_input("Product Name")

# Category selection
category=st.sidebar.selectbox("Category",["Laptop","Mobile","Accessories","Television","Other"])

# Price input
price=st.sidebar.number_input("Price",min_value=0.0,value=0.0)

# Add Product Button
if st.sidebar.button("Add Product"):
        
        # Simple Validation
        if product_name=="":
                st.error("Please Enter the Product name.")
        
        elif price<=0:
                st.error("Please enter a valid price greater than 0")
        else:
# Success Message
                st.success("Product added Successfully")
                
# Display product details
                st.write("### Product Details")
                st.write("Product Name :",product_name)
                st.write("Category :",category)
                st.write("Price ₹:",price)