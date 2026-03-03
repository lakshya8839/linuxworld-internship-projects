import streamlit as st
import requests

# Gemini API Key
API_KEY = "AIzaSyBQ6kbTDsP1WpqGuXBsajJPFEyQTlqAw0Y"  # Replace with your actual key

# Gemini Client (OpenAI-like)
class GeminiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://generativelanguage.googleapis.com/v1beta"
        self.chat = self.Chat(self)

    class Chat:
        def __init__(self, parent):
            self.completions = self.Completions(parent)

        class Completions:
            def __init__(self, parent):
                self.parent = parent

            def create(self, model, messages):
                prompt = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in messages])
                r = requests.post(
                    f"{self.parent.url}/models/{model}:generateContent?key={self.parent.api_key}",
                    json={"contents": [{"parts": [{"text": prompt}]}]}
                )
                r.raise_for_status()
                text = r.json()["candidates"][0]["content"]["parts"][0]["text"]
                
                class Msg: content = text
                class Choice: message = Msg()
                class Response: choices = [Choice()]
                return Response()

client = GeminiClient(api_key=API_KEY)

def suggest(domain, query):
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": f"You are a domain expert in {domain}. Keep advice crisp, practical, and in bullet points."},
            {"role": "user", "content": query},
        ],
    )
    return response.choices[0].message.content

# --- Streamlit UI ---
st.set_page_config(page_title="Gemini Expert Advisor", layout="centered")
st.title("🧠 Gemini Expert Advisor")

domain = st.selectbox("Choose your domain", ["Health", "Sports", "Tech", "Non-Tech", "Startup", "Education"])
question = st.text_area("Ask your question", placeholder="e.g. How can I build a strong startup team?")

if st.button("Get Expert Suggestion"):
    if question.strip():
        with st.spinner("Thinking..."):
            answer = suggest(domain, question)
        st.markdown("### 💡 Expert Advice")
        st.markdown(answer)
    else:
        st.warning("Please enter a question.")
