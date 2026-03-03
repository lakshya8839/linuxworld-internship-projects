import streamlit as st
import platform
import subprocess
import os
from pathlib import Path

# Set page config
st.set_page_config(page_title="AI Tools Hub", layout="wide")

# Sidebar Navigation
st.sidebar.title("AI Tools Navigation")
menu = st.sidebar.radio("Select Tool:", (
    "Local System Commands",
    "Remote SSH Commands",
    "Instagram Post",
    "Send Email",
    "Twilio Voice Call",
    "Twitter Scraper",
    "Web Scraper"
))

system_type = platform.system()

# 1. Local Commands
if menu == "Local System Commands":
    st.title("Local System Command Runner")
    st.info(f"Detected OS: **{system_type}**")

    options = {
        "Get current date": "date",
        "Show calendar (Linux only)": "calendar",
        "Get network configuration": "ipconfig",
        "List current directory files": "list_files",
        "Create a new directory": "mkdir"
    }

    selected = st.selectbox("Available Commands:", list(options.keys()))

    if selected == "Get current date":
        command = "date /T" if system_type == "Windows" else "date"
        try:
            result = subprocess.check_output(command, shell=True).decode().strip()
            st.code(result)
        except Exception as e:
            st.error(f"Error: {e}")

    elif selected == "Show calendar (Linux only)":
        if system_type != "Linux":
            st.warning("The `cal` command only works on Linux.")
        else:
            try:
                result = subprocess.check_output("cal", shell=True).decode().strip()
                st.code(result)
            except Exception as e:
                st.error(f"Error: {e}")

    elif selected == "Get network configuration":
        try:
            if system_type == "Windows":
                result = subprocess.check_output("ipconfig", shell=True).decode(errors="ignore")
            else:
                try:
                    result = subprocess.check_output("ifconfig", shell=True).decode(errors="ignore")
                except:
                    result = subprocess.check_output("ip a", shell=True).decode(errors="ignore")
            st.code(result)
        except Exception as e:
            st.error(f"Error: {e}")

    elif selected == "List current directory files":
        try:
            command = "dir" if system_type == "Windows" else "ls -l"
            result = subprocess.check_output(command, shell=True).decode(errors="ignore")
            st.code(result)
        except Exception as e:
            st.error(f"Error: {e}")

    elif selected == "Create a new directory":
        folder_name = st.text_input("Enter directory name to create:")
        if st.button("Create Directory"):
            try:
                os.makedirs(folder_name, exist_ok=True)
                st.success(f"Directory '{folder_name}' created successfully.")
            except Exception as e:
                st.error(f"Error: {e}")

# 2. SSH Command Runner
elif menu == "Remote SSH Commands":
    import paramiko
    st.title("Remote SSH Linux & Docker Command Executor")

    ssh_ip = st.text_input("SSH Server IP")
    ssh_user = st.text_input("SSH Username")
    ssh_pass = st.text_input("SSH Password", type="password")

    category = st.radio("Choose Command Category", ["Linux Commands", "Docker Commands"])

    linux_commands = [
        "date", "cal", "df -h", "free -m", "uname -a", "whoami", "ip a", "ls -l", "pwd",
        "top -b -n 1", "uptime", "hostname", "netstat -tuln", "ps aux", "id", "history",
        "env", "echo $SHELL", "cat /etc/os-release"
    ]

    docker_commands = [
        "docker ps -a", "docker images", "docker version", "docker info",
        "docker stats --no-stream", "docker network ls", "docker volume ls",
        "docker container ls", "docker system df"
    ]

    selected_command = None
    if category == "Linux Commands":
        selected_command = st.selectbox("Choose a Linux command to run:", linux_commands)
    else:
        selected_command = st.selectbox("Choose a Docker command to run:", docker_commands)

    if st.button("Run on Remote"):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ssh_ip, username=ssh_user, password=ssh_pass)
            stdin, stdout, stderr = client.exec_command(selected_command)
            output = stdout.read().decode().strip()
            errors = stderr.read().decode().strip()
            if output:
                st.code(output)
            if errors:
                st.error(errors)
            client.close()
        except Exception as e:
            st.error(f"Connection Failed: {e}")



# The rest remains unchanged (Instagram, Email, Twilio, Twitter, Web Scraper)...
# 4. Instagram Post
elif menu == "Instagram Post":
    import random, time  
    time.sleep(random.uniform(3, 10))
    from instagrapi import Client
    st.title("Instagram Uploader")
    username = st.text_input("Instagram Username")
    password = st.text_input("Instagram Password", type="password")
    caption = st.text_area("Enter Caption")
    media_path = st.text_input("Image Path (Full)")

    if st.button("Post to Instagram"):
        try:
            cl = Client()
            cl.login(username, password)
            cl.photo_upload(media_path, caption)
            st.success("Posted successfully!")
        except Exception as e:
            st.error(f"Instagram Error: {e}")

# 5. Email Sender
elif menu == "Send Email":
    import smtplib
    from email.mime.text import MIMEText
    st.title("Send Email via SMTP")
    sender = st.text_input("Sender Email")
    password = st.text_input("Sender Password", type="password")
    receiver = st.text_input("Receiver Email")
    subject = st.text_input("Subject")
    body = st.text_area("Message Body")

    if st.button("Send Email"):
        try:
            msg = MIMEText(body, "plain")
            msg["Subject"] = subject
            msg["From"] = sender
            msg["To"] = receiver

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
            server.quit()
            st.success("Email sent successfully")
        except Exception as e:
            st.error(f"Email Error: {e}")

# 6. Twilio Voice Call
elif menu == "Twilio Voice Call":
    from twilio.rest import Client as TwilioClient
    st.title("Twilio Voice Call")
    sid = st.text_input("Account SID")
    auth_token = st.text_input("Auth Token", type="password")
    from_num = st.text_input("From Number (Twilio verified)")
    to_num = st.text_input("To Number")
    msg = st.text_area("Message to Speak")

    if st.button("Make Call"):
        try:
            client = TwilioClient(sid, auth_token)
            call = client.calls.create(
                twiml=f'<Response><Say>{msg}</Say></Response>',
                to=to_num,
                from_=from_num
            )
            st.success(f"Call initiated: {call.sid}")
        except Exception as e:
            st.error(f"Twilio Error: {e}")

# 7. Twitter Scraper
elif menu == "Twitter Scraper":
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from bs4 import BeautifulSoup
    st.title("Twitter Comment Scraper")
    tweet_url = st.text_input("Enter Tweet URL")

    if st.button("Scrape Comments"):
        try:
            options = Options()
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
            driver.get(tweet_url)
            st.info("Loading tweet...")
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            comments = [tag.text for tag in soup.find_all("div") if "@" not in tag.text and len(tag.text) > 20]
            for c in comments:
                st.write("- ", c)
            driver.quit()
        except Exception as e:
            st.error(f"Scraping Error: {e}")

# 8. Web Scraper
elif menu == "Web Scraper":
    import requests
    from bs4 import BeautifulSoup
    st.title("Simple Web Scraper")
    url = st.text_input("Enter Website URL")

    if st.button("Scrape"):
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            st.subheader("Page Title")
            st.write(soup.title.string if soup.title else "No Title")

            st.subheader("Headings Found")
            for h in soup.find_all(["h1", "h2", "h3"]):
                st.write(f"{h.name}: {h.text.strip()}")
        except Exception as e:
            st.error(f"Web Scraper Error: {e}")
