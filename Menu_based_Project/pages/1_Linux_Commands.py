
import streamlit as st
import os

st.title("💻 Linux SSH Commands")

ssh_user = st.text_input("Enter SSH Username")
ssh_ip = st.text_input("Enter SSH IP Address")

commands = {
    "1. Date": "date",
    "2. Calendar": "cal",
    "3. Ifconfig": "ifconfig",
    "4. List Files": "ls",
    "5. Current Directory": "pwd",
}

selected = st.selectbox("Choose a command to run remotely:", list(commands.keys()))

if ssh_user and ssh_ip and st.button("Run Command"):
    cmd = f"ssh {ssh_user}@{ssh_ip} {commands[selected]}"
    output = os.popen(cmd).read()
    st.code(output)
