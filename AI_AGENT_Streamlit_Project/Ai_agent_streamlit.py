import streamlit as st
import subprocess
import platform
import os
import google.generativeai as genai
from langchain.agents import tool
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@tool
def get_date(_: str = "") -> str:
    """Returns the current system date."""
    try:
        command = "date /T" if platform.system() == "Windows" else "date"
        output = subprocess.check_output(command, shell=True)
        return output.decode().strip()
    except Exception as e:
        return f"Failed to get date: {e}"

@tool
def get_calendar(_: str = "") -> str:
    """Returns the current calendar (Linux only)."""
    if platform.system() != "Linux":
        return "The 'cal' command is only available on Linux."
    try:
        output = subprocess.check_output("cal", shell=True)
        return output.decode().strip()
    except Exception as e:
        return f"Failed to get calendar: {e}"

@tool
def get_ip_config(_: str = "") -> str:
    """Shows network configuration."""
    try:
        if platform.system() == "Windows":
            command = "ipconfig"
        else:
            try:
                command = "ifconfig"
                output = subprocess.check_output(command, shell=True)
            except:
                command = "ip a"
                output = subprocess.check_output(command, shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"Failed to get IP config: {e}"

@tool
def list_files(_: str = "") -> str:
    """Lists files in the current directory."""
    try:
        command = "dir" if platform.system() == "Windows" else "ls -l"
        output = subprocess.check_output(command, shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"Failed to list files: {e}"

@tool
def make_directory(dir_name: str) -> str:
    """Creates a directory with the given name."""
    try:
        os.makedirs(dir_name, exist_ok=True)
        return f"Directory '{dir_name}' created successfully."
    except Exception as e:
        return f"Failed to create directory: {e}"

def get_tool_from_query(query: str):
    tool_map = {
        "date": get_date,
        "calendar": get_calendar,
        "cal": get_calendar,
        "ip": get_ip_config,
        "network": get_ip_config,
        "list": list_files,
        "ls": list_files,
        "dir": list_files,
        "make": make_directory,
        "mkdir": make_directory
    }
    for key, func in tool_map.items():
        if key in query.lower():
            return func
    return None

def extract_directory_name(query: str) -> str:
    tokens = query.strip().split()
    for i, word in enumerate(tokens):
        if word.lower() in ["named", "name", "called", "folder"]:
            if i + 1 < len(tokens):
                return tokens[i + 1]
    return "new_folder"

st.set_page_config(page_title="AI Tools", layout="centered")
st.title("AI Tools")

with st.expander("Available Commands", expanded=True):
    st.markdown("""
- **System Date**: `run date`, `get date`
- **Calendar** _(Linux only)_: `get calendar`, `show cal`
- **IP Configuration**: `show ip config`, `network status`, `get ip`
- **List Files**: `list files`, `dir`, `ls`
- **Make Directory**: `make folder named test`, `create directory called logs`
""")

user_input = st.text_input("Enter your command:", placeholder="e.g., run date, list files, create folder named test")

if user_input:
    with st.spinner("Running..."):
        tool_fn = get_tool_from_query(user_input)
        if not tool_fn:
            st.error("No matching tool found.")
        else:
            if tool_fn == make_directory:
                folder_name = extract_directory_name(user_input)
                result = tool_fn.run(folder_name)
            else:
                result = tool_fn.run("")
            st.code(result, language="bash")
