# ✅ Streamlit App to Run Windows/Linux Commands via Tools
import streamlit as st
import paramiko
import subprocess
from langchain.tools import StructuredTool
from pydantic import BaseModel

st.set_page_config(page_title="🖥️ AI Shell Interface", layout="wide")
st.title("🧠 AI Shell Interface: Run Windows & Linux Commands")

# ✅ SSH Helper for Linux Commands
def run_ssh_command(host, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode() + stderr.read().decode()
        ssh.close()
        return output
    except Exception as e:
        return f"SSH Error: {e}"

# ✅ Local Windows Command Runner
def run_windows_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        return result.stdout + result.stderr
    except Exception as e:
        return f"Windows Error: {e}"

# ✅ Schema for SSH Tool
class SSHInput(BaseModel):
    host: str
    username: str
    password: str
    command: str

# ✅ Schema for Windows Tool
class WindowsInput(BaseModel):
    command: str

# ✅ Linux Command Tool
ssh_tool = StructuredTool.from_function(
    name="linux_command_tool",
    description="Run Linux command remotely over SSH.",
    args_schema=SSHInput,
    func=lambda host, username, password, command: run_ssh_command(host, username, password, command)
)

# ✅ Windows Command Tool
windows_tool = StructuredTool.from_function(
    name="windows_command_tool",
    description="Run Windows shell command locally.",
    args_schema=WindowsInput,
    func=lambda command: run_windows_command(command)
)

# ✅ UI
option = st.radio("💻 Select OS", ["Linux (via SSH)", "Windows (Local)"], horizontal=True)

if option == "Linux (via SSH)":
    with st.form("linux_form"):
        host = st.text_input("🔌 Host (e.g. 192.168.1.10)")
        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")
        command = st.text_area("💬 Enter Linux Command")
        submitted = st.form_submit_button("Run Linux Command")
        if submitted:
            result = ssh_tool.run({
                "host": host,
                "username": username,
                "password": password,
                "command": command
            })
            st.code(result, language="bash")

else:
    with st.form("windows_form"):
        command = st.text_area("💬 Enter Windows Command (e.g. dir, mkdir test, echo Hello)")
        submitted = st.form_submit_button("Run Windows Command")
        if submitted:
            result = windows_tool.run({
                "command": command
            })
            st.code(result, language="powershell")

st.markdown("---")
st.markdown("⚙️ Powered by LangChain Tools + Streamlit UI")
