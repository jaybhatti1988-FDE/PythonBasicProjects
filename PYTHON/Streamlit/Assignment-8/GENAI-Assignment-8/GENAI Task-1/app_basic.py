import streamlit as st

# Display title
st.title("Welcome to Streamlit !")

# Text input for name
name=st.text_input(" Enter your name: ")

# Great Me Button
if st.button("Great Me"):
    if name:
        st.write("Hello, ", name+ "!")
    else:
        st.write("Please enter your name")