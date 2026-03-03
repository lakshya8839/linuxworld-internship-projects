import streamlit as st
import platform
import subprocess
import os
import paramiko

# Define local command runner
def run_local_command(cmd: str) -> str:
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return output.decode(errors="ignore")
    except subprocess.CalledProcessError as e:
        return f"❌ Error: {e.output.decode(errors='ignore')}"

# Define SSH command runner
def run_ssh_command(host: str, user: str, password: str, command: str) -> str:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode() + stderr.read().decode()
        client.close()
        return output.strip()
    except Exception as e:
        return f"❌ SSH Error: {e}"

st.set_page_config(page_title="AI System Command Tools", layout="wide")
st.title("🧠 AI Command Toolkit (Windows/Linux + Docker + Web)")

# Sidebar navigation
menu = [
    "🖥️ System Commands",
    "📁 File & Permission Commands",
    "🛠️ User/Admin Commands",
    "📦 Docker (Local)",
    "☁️ Docker (Remote SSH)",
    "🌐 Web Tools",
    "🔧 Setup Commands",
    "🏁 Exit"
]
choice = st.sidebar.selectbox("Select a command category:", menu)

# 🖥️ System Commands
if choice == "🖥️ System Commands":
    st.subheader("System Commands")
    cmd = st.selectbox("Select command:", ["date", "cal (Linux only)", "ipconfig / ifconfig", "ls / dir"])
    if st.button("Run"):
        if cmd == "date":
            result = run_local_command("date /T" if platform.system() == "Windows" else "date")
        elif cmd == "cal (Linux only)":
            result = run_local_command("cal") if platform.system() == "Linux" else "❌ Not supported on Windows"
        elif cmd == "ipconfig / ifconfig":
            result = run_local_command("ipconfig" if platform.system() == "Windows" else "ifconfig || ip a")
        elif cmd == "ls / dir":
            result = run_local_command("dir" if platform.system() == "Windows" else "ls -l")
        st.code(result)

# 📁 File & Permission Commands
elif choice == "📁 File & Permission Commands":
    st.subheader("File & Permission Commands")
    operation = st.selectbox("Select:", ["Create File", "List Permissions", "File Permission (Specific)", "Change File Permissions"])
    if operation == "Create File":
        filename = st.text_input("Enter filename to create:")
        if st.button("Create"):
            try:
                open(filename, 'a').close()
                st.success(f"File '{filename}' created successfully.")
            except Exception as e:
                st.error(str(e))
    elif operation == "List Permissions":
        result = run_local_command("icacls *" if platform.system() == "Windows" else "ls -l")
        st.code(result)
    elif operation == "File Permission (Specific)":
        file = st.text_input("Enter filename:")
        if st.button("Check Permission"):
            cmd = f"icacls {file}" if platform.system() == "Windows" else f"ls -l {file}"
            result = run_local_command(cmd)
            st.code(result)
    elif operation == "Change File Permissions":
        file_mode = st.text_input("Enter chmod value (e.g., 755):")
        filename = st.text_input("Enter filename:")
        if st.button("Change Permission"):
            if platform.system() != "Linux":
                st.error("Only supported on Linux")
            else:
                result = run_local_command(f"chmod {file_mode} {filename}")
                st.code(result)

# 🛠️ User/Admin Commands
elif choice == "🛠️ User/Admin Commands":
    st.subheader("User/Admin Commands")
    action = st.selectbox("Choose:", ["Add User", "Delete User", "Switch User"])
    username = st.text_input("Enter username:")
    if st.button("Execute"):
        if platform.system() != "Linux":
            st.error("This feature is Linux only")
        else:
            if action == "Add User":
                result = run_local_command(f"sudo useradd {username}")
            elif action == "Delete User":
                result = run_local_command(f"sudo userdel {username}")
            elif action == "Switch User":
                result = f"Run manually: su - {username}"
            st.code(result)

# 📦 Docker Local
elif choice == "📦 Docker (Local)":
    st.subheader("Docker (Local)")
    cmd = st.selectbox("Docker Command:", [
        "docker ps", "docker ps -a", "docker images", "docker start", "docker stop", "docker rm", "docker run", "docker pull"
    ])
    arg = st.text_input("Enter container/image name (if applicable):")
    if st.button("Run Docker Command"):
        docker_cmds = {
            "docker ps": "docker ps",
            "docker ps -a": "docker ps -a",
            "docker images": "docker images",
            "docker start": f"docker start {arg}",
            "docker stop": f"docker stop {arg}",
            "docker rm": f"docker rm {arg}",
            "docker pull": f"docker pull {arg}",
            "docker run": f"docker run -dit --name {arg} {arg}"  # Simple run
        }
        cmd_str = docker_cmds[cmd]
        result = run_local_command(cmd_str)
        st.code(result)

# ☁️ Docker Remote SSH
elif choice == "☁️ Docker (Remote SSH)":
    st.subheader("Docker via SSH")
    ssh_host = st.text_input("Remote Host")
    ssh_user = st.text_input("Username")
    ssh_pass = st.text_input("Password", type="password")
    remote_cmd = st.text_input("Docker Command (e.g., docker ps, docker start <id>)")
    if st.button("Run SSH Docker Command"):
        result = run_ssh_command(ssh_host, ssh_user, ssh_pass, remote_cmd)
        st.code(result)

# 🌐 Web Tools
elif choice == "🌐 Web Tools":
    import requests
    from bs4 import BeautifulSoup

    st.subheader("Scrape Website for Headings and Paragraphs")
    url = st.text_input("Enter website URL:")
    if st.button("Scrape"):
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            headings = [h.get_text() for h in soup.find_all(['h1', 'h2'])]
            paras = [p.get_text() for p in soup.find_all('p')]
            st.write("## 🟩 Headings")
            for h in headings:
                st.write("-", h)
            st.write("## 🟦 Paragraphs")
            for p in paras:
                st.write(p)
        except Exception as e:
            st.error(f"Failed to scrape: {e}")

# 🔧 Setup Commands (e.g., yum install, ssh-keygen, minikube)
elif choice == "🔧 Setup Commands":
    st.subheader("System Setup Tools")
    tool = st.selectbox("Choose setup task:", [
        "yum install httpd", "yum install httpd -y", "rpm -q httpd",
        "systemctl start httpd", "systemctl stop firewalld", "systemctl enable httpd",
        "systemctl restart httpd", "systemctl status httpd", "ssh-keygen -t rsa",
        "scp file.txt user@host:/path", "minikube version", "minikube start"
    ])
    if st.button("Run Setup Command"):
        result = run_local_command(tool)
        st.code(result)

# 🏁 Exit
elif choice == "🏁 Exit":
    st.warning("You have exited the AI Command Toolkit.")
