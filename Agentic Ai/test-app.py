import streamlit as st
from langchain.agents import tool
import subprocess
import platform
import os
import paramiko

# ------------------------ LangChain Tools ------------------------

@tool
def get_date(_: str = "") -> str:
    """📅 Returns the current system date."""
    try:
        cmd = "date /T" if platform.system() == "Windows" else "date"
        output = subprocess.check_output(cmd, shell=True)
        return output.decode().strip()
    except Exception as e:
        return f"❌ Failed to get date: {e}"

@tool
def get_calendar(_: str = "") -> str:
    """🗓️ Returns the calendar using `cal` (Linux only)."""
    if platform.system() != "Linux":
        return "❌ The `cal` command is only available on Linux."
    try:
        output = subprocess.check_output("cal", shell=True)
        return output.decode().strip()
    except Exception as e:
        return f"❌ Failed to get calendar: {e}"

@tool
def get_ip_config(_: str = "") -> str:
    """🌐 Shows network configuration."""
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output("ipconfig", shell=True)
        else:
            try:
                output = subprocess.check_output("ifconfig", shell=True)
            except:
                output = subprocess.check_output("ip a", shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Failed to get IP config: {e}"

@tool
def list_files(_: str = "") -> str:
    """📁 Lists files in the current directory."""
    try:
        cmd = "dir" if platform.system() == "Windows" else "ls -l"
        output = subprocess.check_output(cmd, shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Failed to list files: {e}"

@tool
def make_directory(dir_name: str) -> str:
    """📂 Creates a new directory."""
    try:
        os.makedirs(dir_name, exist_ok=True)
        return f"✅ Directory '{dir_name}' created successfully."
    except Exception as e:
        return f"❌ Failed to create directory: {e}"

@tool
def add_user(username: str) -> str:
    """👤 Adds a new system user (Linux only)."""
    if platform.system() != "Linux":
        return "❌ The `useradd` command is only supported on Linux."
    try:
        subprocess.run(["sudo", "useradd", username], check=True)
        return f"✅ User '{username}' added successfully."
    except Exception as e:
        return f"❌ Failed to add user: {e}"

@tool
def delete_user(username: str) -> str:
    """❌ Deletes a user (Linux only)."""
    if platform.system() != "Linux":
        return "❌ The `userdel` command is only supported on Linux."
    try:
        subprocess.run(["sudo", "userdel", username], check=True)
        return f"✅ User '{username}' deleted successfully."
    except Exception as e:
        return f"❌ Failed to delete user: {e}"

@tool
def list_all_permissions(_: str = "") -> str:
    """🔐 Lists all file permissions."""
    try:
        cmd = "icacls *" if platform.system() == "Windows" else "ls -l"
        output = subprocess.check_output(cmd, shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Failed to list permissions: {e}"

@tool
def show_file_permissions(filename: str) -> str:
    """🔍 Shows permissions of a specific file."""
    try:
        cmd = f"icacls {filename}" if platform.system() == "Windows" else f"ls -l {filename}"
        output = subprocess.check_output(cmd, shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Failed to get file permissions: {e}"

@tool
def change_file_permissions(input_str: str) -> str:
    """✏️ Changes file permissions (Linux only)."""
    if platform.system() != "Linux":
        return "❌ chmod is only supported on Linux."
    try:
        mode, file = input_str.strip().split()
        subprocess.run(["chmod", mode, file], check=True)
        return f"✅ Permissions changed to {mode} for {file}"
    except Exception as e:
        return f"❌ Failed to change permissions: {e}"

@tool
def create_file(filename: str) -> str:
    """📄 Creates a new empty file."""
    try:
        open(filename, 'a').close()
        return f"✅ File '{filename}' created successfully."
    except Exception as e:
        return f"❌ Failed to create file: {e}"

@tool
def change_directory(dir_name: str) -> str:
    """📁 Changes current directory."""
    try:
        os.chdir(dir_name)
        return f"✅ Changed directory to: {os.getcwd()}"
    except Exception as e:
        return f"❌ Failed to change directory: {e}"

@tool
def switch_user(username: str) -> str:
    """👤 Switches to another user (Linux only)."""
    if platform.system() != "Linux":
        return "❌ `su` is Linux-only."
    return f"🔒 Run manually in terminal: su - {username}"

@tool
def pip_install(lib: str) -> str:
    """📦 Installs a Python package."""
    try:
        subprocess.run(["pip", "install", lib], check=True)
        return f"✅ Installed: {lib}"
    except Exception as e:
        return f"❌ Failed to install {lib}: {e}"

@tool
def open_notepad(file: str) -> str:
    """📝 Opens a file in Notepad (Windows only)."""
    if platform.system() != "Windows":
        return "❌ Notepad is Windows-only."
    try:
        subprocess.Popen(["notepad", file])
        return f"✅ Opening {file} in Notepad..."
    except Exception as e:
        return f"❌ Failed to open Notepad: {e}"

@tool
def open_gedit(file: str) -> str:
    """📝 Opens a file in gedit (Linux only)."""
    if platform.system() != "Linux":
        return "❌ gedit is Linux-only."
    try:
        subprocess.Popen(["gedit", file])
        return f"✅ Opening {file} in gedit..."
    except Exception as e:
        return f"❌ Failed to open gedit: {e}"

@tool
def open_vim(file: str) -> str:
    """⌨️ Opens a file in Vim (Linux only)."""
    if platform.system() != "Linux":
        return "❌ Vim is Linux-only."
    return f"📝 Run manually in terminal: vim {file}"

# ------------------------ Local Match & Run ------------------------

def match_and_run(user_input: str) -> str:
    user_input = user_input.lower()
    if "date" in user_input:
        return get_date.invoke("")
    elif "calendar" in user_input or "cal" in user_input:
        return get_calendar.invoke("")
    elif "ip" in user_input or "network" in user_input:
        return get_ip_config.invoke("")
    elif "list files" in user_input or "ls" in user_input or "dir" in user_input:
        return list_files.invoke("")
    elif "make directory" in user_input or "mkdir" in user_input:
        return make_directory.invoke(user_input.split()[-1])
    elif "add user" in user_input:
        return add_user.invoke(user_input.split()[-1])
    elif "delete user" in user_input:
        return delete_user.invoke(user_input.split()[-1])
    elif "permissions" in user_input and "all" in user_input:
        return list_all_permissions.invoke("")
    elif "permissions" in user_input:
        return show_file_permissions.invoke(user_input.split()[-1])
    elif "change permission" in user_input:
        parts = user_input.split()
        return change_file_permissions.invoke(f"{parts[-2]} {parts[-1]}")
    elif "create file" in user_input:
        return create_file.invoke(user_input.split()[-1])
    elif "change directory" in user_input or "cd" in user_input:
        return change_directory.invoke(user_input.split()[-1])
    elif "switch user" in user_input:
        return switch_user.invoke(user_input.split()[-1])
    elif "install" in user_input and "pip" in user_input:
        return pip_install.invoke(user_input.split()[-1])
    elif "notepad" in user_input:
        return open_notepad.invoke(user_input.split()[-1])
    elif "gedit" in user_input:
        return open_gedit.invoke(user_input.split()[-1])
    elif "vim" in user_input:
        return open_vim.invoke(user_input.split()[-1])
    else:
        return "❌ Command not recognized. Try a different input."

# ------------------------ Streamlit UI ------------------------

st.set_page_config(page_title="🧠 System + SSH Assistant", layout="centered")
st.title("🧠 System Assistant with SSH (Natural Language)")

st.subheader("💻 Run Local System Commands")

user_input = st.text_input("🗣️ Say what you want (e.g., 'show calendar')")
if user_input:
    st.code(match_and_run(user_input))

# ------------------------ SSH Section ------------------------

st.markdown("---")
st.subheader("🐧 Run Remote Linux Commands over SSH")

def parse_ssh_intent(phrase: str) -> str:
    phrase = phrase.lower()
    if "calendar" in phrase or "cal" in phrase:
        return "cal"
    elif "date" in phrase:
        return "date"
    elif "ip" in phrase:
        return "ip a"
    elif "memory" in phrase:
        return "free -h"
    elif "disk" in phrase or "space" in phrase:
        return "df -h"
    elif "files" in phrase or "ls" in phrase:
        return "ls -l"
    elif "whoami" in phrase:
        return "whoami"
    elif "uptime" in phrase:
        return "uptime"
    elif "os" in phrase:
        return "cat /etc/os-release"
    else:
        return ""

with st.form("ssh_form"):
    ssh_host = st.text_input("🔌 SSH Host (e.g., 192.168.1.100)")
    ssh_user = st.text_input("👤 SSH Username")
    ssh_pass = st.text_input("🔑 SSH Password", type="password")
    ssh_phrase = st.text_input("🗣️ What to run? (e.g., 'show ip')")
    run_btn = st.form_submit_button("Run via SSH")

if run_btn:
    ssh_cmd = parse_ssh_intent(ssh_phrase)
    if not all([ssh_host, ssh_user, ssh_pass, ssh_cmd]):
        st.error("❗ Missing field or unrecognized command.")
    else:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ssh_host, username=ssh_user, password=ssh_pass)
            stdin, stdout, stderr = ssh.exec_command(ssh_cmd)
            output = stdout.read().decode()
            error = stderr.read().decode()
            ssh.close()

            if output:
                st.success("✅ SSH Output:")
                st.code(output)
            if error:
                st.error("⚠️ SSH Error:")
                st.code(error)
        except Exception as e:
            st.error(f"❌ SSH Failed: {e}")
