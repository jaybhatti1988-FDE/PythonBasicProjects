import streamlit as st
st.write("Hello Python Gen AI community...!")
st.title("GEN AI")
st.write("This is my First Streamlit site")
st.header("Streamlit AI")
st.subheader("Subheader Streamlit")
st.text("Streamlit Plain Text")

# button

if st.button("Click Me..!"):
    st.write("Button Clicked...!")

# checkbox

agree_chekbx=st.checkbox("I agree above policy")

if agree_chekbx:
    st.write("You Accept Policy Successfully")

# Slider

lvl=st.slider("Check IQ level ",1,10,5)
st.write(f"Select level : {lvl}")

# uload file

uploaded_file=st.file_uploader("upload a file",type=["csv","txt","pdf","png"])

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df.head())
