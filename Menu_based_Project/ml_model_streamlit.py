import streamlit as st
from sklearn.linear_model import LinearRegression
st.title("Marks Obtained Model")
st.write("The model predict your marks based on score!!")
y=st.slider("Hours you studied",1,10)

import pandas
dataset = pandas.read_csv("marks.csv")
marks = dataset['marks']
marks = marks.values.reshape(-1, 1)
hrs = dataset['hrs']
hrs = hrs.values.reshape(-1, 1)   
brain = LinearRegression()
brain.fit(hrs,marks)
z=brain.predict([[y]])  
st.write("your marks obtained",z)