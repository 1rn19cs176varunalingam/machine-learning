import streamlit as st
import joblib
st.title("SPAM HAM CLASSIFIER")
ip=st.text_input("enter you message:")
op=text_model.predict([ip])
if st.button('perdict'):
  st.title(op[0])
