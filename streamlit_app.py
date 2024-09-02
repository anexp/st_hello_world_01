import streamlit as st
import yfinance as yf

st.title('Machine Learning App')

st.write('Hello World from streamlit')

num1 = st.number_input(label="Number 1")
num2 = st.number_input(label="Number 2")

st.write("Operation")

operation = st.radio("Select an operation",("Add","Subtract","Multiply","Divide"))

ans = 0

def calculate():
    if operation == "Add":
        ans = num1 + num2
    elif operation == "Subtract":
        ans = num1 - num2
    elif operation == "Multiply":
        ans = num1 * num2
    elif operation == "Divide" :
        if num2 == 0:
            ans = "Not defined"
        else :
            ans = num1/num2
    else :
        st.warning("Undefined operation")
        ans = "Not Defined"

    st.success(f'Answer = {ans}')

if st.button("Calculate result"):
   calculate()

