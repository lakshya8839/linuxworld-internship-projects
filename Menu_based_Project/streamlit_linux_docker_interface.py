
import streamlit as st
import os
import getpass

st.set_page_config(page_title="Linux + Docker + Automation Menu", layout="centered")

st.title("🚀 Linux + Docker + Automation Interface")
mode = st.radio("Choose Execution Mode", ["Remote via SSH", "Local/Windows Only"])

if mode == "Remote via SSH":
    ssh_user = st.text_input("Enter SSH Username")
    ssh_ip = st.text_input("Enter SSH IP Address")
    if not ssh_user or not ssh_ip:
        st.warning("Please provide both SSH username and IP to proceed.")
    else:
        st.subheader("📡 SSH-Based Commands")
        cmd = st.selectbox("Choose a command", [
            "Date", "Cal", "Ifconfig", "List Files", "Make Directory", "Add User",
            "Delete User", "List All File Permissions", "Check File Permission",
            "Change File Permission", "Create File", "Change Directory",
            "Change User (sudo)", "pip install", "gedit", "vim", "YUM Config",
            "ssh-keygen", "SCP File", "Minikube Setup", "Start Minikube",
            "Install Apache", "Check Apache", "Auto Apache Install", "Start Apache",
            "Apache Status", "Stop Firewall", "Enable Apache", "Restart Apache",
            "Docker Launch", "Docker Start", "Docker Stop", "Docker Remove",
            "List Docker Images", "List Containers", "Docker Pull"
        ])

        if cmd == "Date":
            st.code(os.popen(f"ssh {ssh_user}@{ssh_ip} date").read())
        elif cmd == "Cal":
            st.code(os.popen(f"ssh {ssh_user}@{ssh_ip} cal").read())
        elif cmd == "Ifconfig":
            st.code(os.popen(f"ssh {ssh_user}@{ssh_ip} ifconfig").read())
        elif cmd == "List Files":
            st.code(os.popen(f"ssh {ssh_user}@{ssh_ip} ls").read())
        elif cmd == "Make Directory":
            dir_name = st.text_input("Enter directory name")
            if st.button("Create Directory"):
                st.code(os.popen(f"ssh {ssh_user}@{ssh_ip} mkdir {dir_name}").read())
        elif cmd == "Add User":
            new_user = st.text_input("New username")
            if st.button("Add User"):
                st.code(os.popen(f"ssh {ssh_user}@{ssh_ip} useradd {new_user}").read())
        elif cmd == "Delete User":
            del_user = st.text_input("Username to delete")
            if st.button("Delete User"):
                st.code(os.popen(f"ssh {ssh_user}@{ssh_ip} userdel {del_user}").read())
        elif cmd == "List All File Permissions":
            st.code(os.popen(f"ssh {ssh_user}@{ssh_ip} ls -l").read())
        elif cmd == "Check File Permission":
            fname = st.text_input("Enter filename")
            if st.button("Check"):
                st.code(os.popen(f"ssh {ssh_user}@{ssh_ip} ls -l {fname}").read())
        elif cmd == "Change File Permission":
            f = st.text_input("File name")
            who = st.selectbox("Permission to", ["u", "g", "o"])
            op = st.selectbox("Operation", ["+", "-"])
            perm = st.text_input("Permissions (rwx)")
            if st.button("Change Permission"):
                st.code(os.popen(f"ssh {ssh_user}@{ssh_ip} chmod {who}{op}{perm} {f}").read())
        # More commands can be added similarly...

elif mode == "Local/Windows Only":
    st.subheader("💻 Local / Windows Commands")
    cmd = st.selectbox("Choose a command", [
        "List Docker Images", "Pull Docker Image", "Instagram Post (Single)",
        "Send Email", "Voice Call (Twilio)", "Web Scraping", "Open Notepad"
    ])

    if cmd == "List Docker Images":
        st.code(os.popen("docker images").read())
    elif cmd == "Pull Docker Image":
        image = st.text_input("Enter Docker image name")
        if st.button("Pull Image"):
            st.code(os.popen(f"docker pull {image}").read())
    elif cmd == "Open Notepad":
        fname = st.text_input("File name")
        if st.button("Open"):
            os.system(f"notepad {fname}")
    elif cmd == "Web Scraping":
        import requests
        from bs4 import BeautifulSoup
        url = st.text_input("Enter website URL")
        if st.button("Scrape"):
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            headings = soup.find_all(['h1','h2','h3','h4','h5','h6'])
            paragraphs = soup.find_all('p')
            st.write("### Headings")
            for tag in headings:
                st.write(tag.text.strip())
            st.write("### Paragraphs")
            for p in paragraphs:
                st.write(p.text.strip())
