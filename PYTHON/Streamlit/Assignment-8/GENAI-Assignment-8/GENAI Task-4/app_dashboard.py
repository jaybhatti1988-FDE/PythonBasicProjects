import streamlit as st

# Title
st.title("Simple Sales Dashboard")

# Description
st.write("Select a month to view the sales details. ")

# List of Months
months=["January","February","March","April"]

# Static monthly sales data
sales={
        "January":1200,
        "February":1500,
        "March":900,
        "April":2000
       }

# Select Month
selected_month=st.selectbox(" Selected Month: ",months)

# Display selected month's sales
st.metric(label=f"{selected_month} Sales",value=sales[selected_month])

# Display Bar chart
st.write("### Monthly Sales Chart")
st.bar_chart(list(sales.values()))