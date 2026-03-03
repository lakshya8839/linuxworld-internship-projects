import streamlit as st
import joblib

model = joblib.load("my_salary_model.pkl")
st.title("Employee Salary Prediction Based On Experience")
st.write("Enter your Experience:")

Exp = st.number_input("Enter your Experience:", min_value=1, max_value=25 )

if st.button("Predict"):
    result = model.predict([[Exp]])
    st.write(f"Your salary is ₹{result[0]:,.2f}")
