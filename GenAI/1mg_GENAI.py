import streamlit as st

import requests

from bs4 import BeautifulSoup

from openai import OpenAI

import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load the environment variables from .env
load_dotenv()

# API key for Gemini (you should consider using st.secrets in real apps for security)

gemini_api_key = os.getenv("GEMINI_API_KEY")



# Get content from 1mg

response = requests.get("https://www.1mg.com")

htmlaicontent = response.text

mysoup = BeautifulSoup(markup=htmlaicontent, features="html.parser")



# Set up the Gemini model through OpenAI interface

gemini_model = OpenAI(

    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",

    api_key=gemini_api_key

)



# Define the chatbot function

def chatbot(userprompt):

    my_msg = [

        {"role": "system", "content": f"you are AI assistent, your duty is to give the information about medicines available or not and thier salts ,take your content from: {htmlaicontent}"},

        {"role": "user", "content": userprompt}

    ]

    response = gemini_model.chat.completions.create(model="gemini-2.5-flash", messages=my_msg)

    return response.choices[0].message.content



# Streamlit UI

st.title("Medicine Info Chatbot (Gemini)")



user_input = st.text_input("Ask about any medicine:", placeholder="e.g., tell me about paracetamol")



if user_input:

    with st.spinner("Thinking..."):

        answer = chatbot(user_input)

    st.markdown("### Answer:")

    st.write(answer)