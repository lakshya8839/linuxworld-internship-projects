import streamlit as st

st.set_page_config(page_title="🚀 Project Dashboard", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
        body {
            overflow-x: hidden;
        }
        .stApp {
            background-color: #0f2027;
            background-image: linear-gradient(315deg, #0f2027, #203a43, #2c5364);
            color: white;
        }
        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 2rem;
            padding: 2rem 1rem;
        }
        .card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 20px;
            transition: all 0.3s ease;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            backdrop-filter: blur(10px);
        }
        .card:hover {
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 12px 24px rgba(0,0,0,0.4);
        }
        .card-title {
            font-size: 1.4rem;
            color: #00ffe1;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        .card-description {
            font-size: 1rem;
            margin-bottom: 1.2rem;
            color: #dddddd;
        }
        .card-buttons {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        .stButton > button {
            background-color: #003e5c;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            font-size: 15px;
            font-weight: 600;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background-color: #0083b0;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown("<h1 style='text-align: center; color: #00ffe1;'>🧭 CommandHub – Unified Project Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1rem; color: white;'>Explore and interact with all tools from one beautiful interface</p>", unsafe_allow_html=True)
st.markdown("---")

# ---------- Start Grid ----------
st.markdown('<div class="project-grid">', unsafe_allow_html=True)

# ---------- Project 1 ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">1️⃣ Linux SSH Command Executor</div>', unsafe_allow_html=True)
st.markdown('<div class="card-description">Run Linux terminal commands on remote systems using a secure SSH interface.</div>', unsafe_allow_html=True)
if st.button("🔧 Launch", key="ssh"):
    st.switch_page("pages/1_All_Commands.py")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Project 2 ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">2️⃣ Windows / Docker Command App</div>', unsafe_allow_html=True)
st.markdown('<div class="card-description">Control Windows/Docker tools from the browser. Useful for automation or education.</div>', unsafe_allow_html=True)
if st.button("🪟 Launch", key="win"):
    st.switch_page("pages/6_frontpage.py")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Project 3 ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">3️⃣ ML Marks Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="card-description">Enter study hours and get marks prediction using a trained ML model.</div>', unsafe_allow_html=True)
if st.button("📊 Predict Now", key="ml"):
    st.switch_page("pages/3_ML_Predict_Marks.py")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Project 4 ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">4️⃣ GenAI Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="card-description">Conversational AI assistant using Gemini/OpenAI. Great for Q&A or document help.</div>', unsafe_allow_html=True)
if st.button("🤖 Launch", key="genai"):
    st.switch_page("pages/5_GenAI_Project.py")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Project 5 ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">5️⃣ GitHub + LinkedIn Showcase</div>', unsafe_allow_html=True)
st.markdown('<div class="card-description">Quick access to your portfolio links with custom branding and buttons.</div>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    st.link_button("🌐 GitHub", "https://github.com/yourprofile")
with col2:
    st.link_button("💼 LinkedIn", "https://linkedin.com/in/yourprofile")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- End Grid ----------
st.markdown('</div>', unsafe_allow_html=True)
