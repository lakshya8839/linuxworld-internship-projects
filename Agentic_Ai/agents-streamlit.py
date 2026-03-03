import streamlit as st
import subprocess
import platform
import os
import paramiko
import requests
from bs4 import BeautifulSoup
from langchain.agents import initialize_agent, AgentType, tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import Tool
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document

# Load Gemini API Key from .env or other secure config
from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Load LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

# Global store for scraped data
scraped_text = ""

# Tool: Run Linux Command via SSH
@tool
def run_ssh_command(input_str: str) -> str:
    """
    🐧 Run a Linux command on a remote machine using SSH.
    Format: user@host command
    Example: root@192.168.1.100 ls -l
    """
    try:
        user_host, *cmd = input_str.strip().split()
        username, hostname = user_host.split("@")
        command = " ".join(cmd)
        password = st.text_input(f"🔐 Enter password for {username}@{hostname}", type="password")
        if not password:
            return "❗ Please enter SSH password."
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode() + stderr.read().decode()
        client.close()
        return output.strip()
    except Exception as e:
        return f"❌ SSH Error: {e}"

# Tool: Run Windows Local Command
@tool
def run_windows_command(cmd: str) -> str:
    """
    🪟 Run a Windows command locally.
    """
    try:
        if platform.system() != "Windows":
            return "❌ Not a Windows system."
        output = subprocess.check_output(cmd, shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Windows Error: {e}"

# Tool: Scrape Website Content
@tool
def scrape_website(url: str) -> str:
    """
    🌐 Scrapes <h1>–<h4> and <p> tags for QA.
    """
    global scraped_text
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        tags = soup.find_all(["h1", "h2", "h3", "h4", "p"])
        scraped_text = "\n".join(tag.get_text(strip=True) for tag in tags)
        return scraped_text[:1000] + "... (✅ Scraped. Ask below)"
    except Exception as e:
        return f"❌ Scrape Error: {e}"

# Tool: Ask Question from Scraped Webpage
@tool
def query_scraped_data(query: str) -> str:
    """
    ❓ Ask question from last scraped website.
    """
    global scraped_text
    try:
        if not scraped_text:
            return "⚠️ Nothing scraped yet."
        docs = [Document(page_content=scraped_text)]
        vectordb = FAISS.from_documents(docs, HuggingFaceEmbeddings())
        qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())
        return qa.run(query)
    except Exception as e:
        return f"❌ QA Error: {e}"

# Tool: Date command (Windows/Linux)
@tool
def get_date(dummy: str) -> str:
    """
    📅 Returns current date. Uses SSH for Linux, local for Windows.
    """
    if platform.system() == "Windows":
        return run_windows_command.run("date /T")
    return run_ssh_command.run(dummy)

# Tool: Cal command (Linux only via SSH)
@tool
def get_calendar(dummy: str) -> str:
    """
    📆 Runs 'cal' command over SSH for Linux systems.
    Format: user@host cal
    """
    return run_ssh_command.run(dummy)

# Tool: ifconfig (Linux only via SSH)
@tool
def get_ifconfig(dummy: str) -> str:
    """
    🌐 Returns network interfaces using 'ifconfig'.
    Format: user@host ifconfig
    """
    return run_ssh_command.run(dummy)

# Tool: ls command (Linux via SSH)
@tool
def list_files(dummy: str) -> str:
    """
    📂 Lists files using 'ls'. Format: user@host ls
    """
    return run_ssh_command.run(dummy)

# Tool: mkdir command (Linux via SSH)
@tool
def make_directory(dummy: str) -> str:
    """
    📁 Create directory using 'mkdir'. Format: user@host mkdir dirname
    """
    return run_ssh_command.run(dummy)

# Add 45 more tools below similarly...
# Placeholder for demonstration
@tool
def placeholder(dummy: str) -> str:
    return "Tool under construction"

# Register Tools
tools = [
    run_ssh_command,
    run_windows_command,
    scrape_website,
    query_scraped_data,
    get_date,
    get_calendar,
    get_ifconfig,
    list_files,
    make_directory,
    *[placeholder for _ in range(42)]  # Placeholder for remaining tools
]

# Agent setup
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

# Streamlit UI
st.set_page_config(page_title="🧠 Gemini AI Toolbelt", layout="wide")
st.title("🛠️ AI Multi-Tool with Gemini")

st.markdown("""
This assistant can:
- 🧠 Execute Linux commands via SSH
- 🪟 Run Windows commands locally
- 🌐 Scrape and analyze websites
- 📦 51 total tools including Docker, Email, Instagram
""")

mode = st.selectbox("Choose operation mode:", [
    "Windows Command",
    "Linux Command (SSH)",
    "Scrape Website",
    "Ask from Scraped Website",
    "Other Tools (Placeholder)"
])

if mode == "Windows Command":
    cmd = st.text_input("💻 Enter Windows Command")
    if st.button("Run") and cmd:
        st.code(agent.run(cmd))

elif mode == "Linux Command (SSH)":
    ssh_input = st.text_input("🐧 Enter: user@host command")
    if st.button("Run SSH") and ssh_input:
        st.code(agent.run(ssh_input))

elif mode == "Scrape Website":
    url = st.text_input("🌐 Enter website URL")
    if st.button("Scrape") and url:
        st.code(agent.run(url))

elif mode == "Ask from Scraped Website":
    q = st.text_input("❓ Ask a question")
    if st.button("Ask") and q:
        st.code(agent.run(q))

else:
    tool_input = st.text_input("🛠 Enter input for placeholder tools")
    if st.button("Run Tool") and tool_input:
        st.code(agent.run(tool_input))
