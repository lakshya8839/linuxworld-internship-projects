import streamlit as st
import os
import subprocess
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="All Commands Interface", layout="centered")
st.title("🧾 All Commands Interface")

mode = st.radio("Where to Run Commands?", ["🔗 SSH (Linux)", "💻 Local (Windows)"])

# SSH config
ssh_user = ""
ssh_ip = ""
if mode == "🔗 SSH (Linux)":
    ssh_user = st.text_input("SSH Username")
    ssh_ip = st.text_input("SSH IP Address")

# Command Dictionary
cmds = {
    "1. date": "date",
    "2. cal": "cal",
    "3. ifconfig": "ifconfig",
    "4. ls": "ls",
    "5. mkdir": "mkdir",
    "6. useradd": "useradd",
    "7. userdel": "userdel",
    "8. ls -l": "ls -l",
    "9. file permission (ls -l <file>)": "ls -l",
    "10. chmod": "chmod",
    "11. touch": "touch",
    "12. cd": "cd",
    "13. sudo su": "sudo su",
    "14. pip install": "pip install",
    "15. gedit": "gedit",
    "16. vim": "vim",
    "17. yum config": "yum-config-manager",
    "18. ssh-keygen": "ssh-keygen -t rsa",
    "19. scp": "scp",
    "20. Minikube setup": "echo 'Set env for Minikube'",
    "21. Minikube start": "minikube start",
    "22. yum install httpd": "yum install httpd",
    "23. rpm -q httpd": "rpm -q httpd",
    "24. yum install httpd -y": "yum install httpd -y",
    "25. systemctl start httpd": "systemctl start httpd",
    "26. systemctl status httpd": "systemctl status httpd",
    "27. stop firewall": "systemctl stop firewalld",
    "28. enable httpd": "systemctl enable httpd",
    "29. restart httpd": "systemctl restart httpd",
    "30. docker run": "docker run",
    "31. docker start": "docker start",
    "32. docker stop": "docker stop",
    "33. docker rm": "docker rm",
    "34. docker images": "docker images",
    "35. docker ps -a": "docker ps -a",
    "36. docker pull": "docker pull",
    "37. local docker run": "docker run",
    "38. local docker start": "docker start",
    "39. local docker stop": "docker stop",
    "40. local docker rm": "docker rm",
    "41. local docker images": "docker images",
    "42. local docker ps -a": "docker ps -a",
    "43. local docker pull": "docker pull",
    "44. insta single post": "insta_single",
    "45. insta multi post": "insta_multi",
    "46. send email": "send_email",
    "47. voice call": "voice_call",
    "48. tweet reader": "tweet_read",
    "49. web scraping": "web_scrape",
    "50. notepad open": "notepad",
    "51. exit": "exit"
}

choice = st.selectbox("Choose a command", list(cmds.keys()))
run = st.button("Run Command")

# Helper function to run local commands safely
def run_local_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return e.output

# Run the command
if run:
    action = cmds[choice]

    if mode == "🔗 SSH (Linux)":
        if not ssh_user or not ssh_ip:
            st.error("Please enter SSH username and IP.")
        else:
            param = ""
            if action in ["mkdir", "useradd", "userdel", "touch", "gedit", "vim", "cd", "pip install", "chmod"]:
                param = st.text_input(f"Enter argument for `{action}`")
            if action == "scp":
                source = st.text_input("Source File Path:")
                dest = st.text_input("Destination (user@ip:/path):")
                if source and dest:
                    os.system(f"scp {source} {dest}")
                    st.success("File copied via SCP")
            elif action == "ssh-keygen -t rsa":
                st.code(os.popen(f"ssh {ssh_user}@{ssh_ip} {action}").read())
            else:
                ssh_command = f"ssh {ssh_user}@{ssh_ip} {action} {param}" if param else f"ssh {ssh_user}@{ssh_ip} {action}"
                st.code(os.popen(ssh_command).read())

    else:  # Local (Windows) Execution
        if action in ["insta_single", "insta_multi", "send_email", "voice_call", "tweet_read"]:
            st.warning(f"`{action}` logic to be implemented.")
        elif action == "web_scrape":
            url = st.text_input("Website URL to scrape:")
            if url:
                r = requests.get(url)
                soup = BeautifulSoup(r.text, "html.parser")
                st.markdown("### Headings")
                for tag in soup.find_all(['h1','h2','h3']):
                    st.markdown(f"- {tag.text.strip()}")
                st.markdown("### Paragraphs")
                for p in soup.find_all("p"):
                    st.write(p.text.strip())
        elif action == "notepad":
            os.system("notepad")
            st.success("Notepad opened successfully.")
        elif action == "exit":
            st.info("Exit chosen. Close the app manually.")
        else:
            param = ""
            if action in ["mkdir", "useradd", "userdel", "touch", "gedit", "vim", "cd", "pip install", "chmod", "docker run", "docker start", "docker stop", "docker rm", "docker pull"]:
                param = st.text_input(f"Enter argument for `{action}`")
            full_cmd = f"{action} {param}" if param else action
            output = run_local_command(full_cmd)
            st.code(output)