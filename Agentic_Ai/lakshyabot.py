
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import streamlit as st
import google.generativeai as genai
import os
import time
from dotenv import load_dotenv

load_dotenv()

# ✅ Gemini API key setup
api_key = os.getenv("GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash")

# ✅ JS-rendered content using Selenium + Service
@st.cache_data(show_spinner=False)
def get_rendered_portfolio_text(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # ✅ Correct way to use Service with ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(5)  # allow time for JS to load

    soup = BeautifulSoup(driver.page_source, "html.parser")
    text = soup.get_text(separator="\n", strip=True)
    driver.quit()
    return text

# ✅ Load website content
portfolio_url = "https://lakshya-chalana-portfolio.netlify.app/"
portfolio_text = get_rendered_portfolio_text(portfolio_url)

# ✅ Gemini prompt logic
def answer_about_portfolio(user_query):
    prompt = f"""
You are MyBuddy, a helpful AI assistant designed to answer questions about Lakshya Chalana based on her portfolio website.

Here is the content from her site:
---
{portfolio_text}
---

Now, answer the following question clearly and informatively:
{user_query}
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠ Gemini Error: {e}"

# ✅ Streamlit UI
st.set_page_config(page_title="🤖 LakshyaBot: Portfolio Chat Assistant", layout="centered")
st.title("🤖 LakshyaBot: Portfolio Chat Assistant")
st.markdown("Ask anything about *Lakshya Chalana’s* projects, experience, skills, or education — powered by her live website.")

user_input = st.text_input("💬 Ask your question:", placeholder="e.g., What are lakshya's projects?")

if user_input:
    with st.spinner("Analyzing lakshya's portfolio..."):
        result = answer_about_portfolio(user_input)
    st.success("✅ Gemini's Answer:")
    st.write(result)