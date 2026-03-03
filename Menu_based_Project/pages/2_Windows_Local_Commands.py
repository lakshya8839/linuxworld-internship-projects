
import streamlit as st
import os

st.title("🪟 Windows / Local Commands")

cmd = st.selectbox("Choose a local command to run:", [
    "1. Notepad", "2. Docker Images", "3. Docker PS", "4. Docker Pull", 
    "5. Start Docker Container", "6. Stop Docker Container"
])

if cmd == "1. Notepad":
    file = st.text_input("File name:")
    if st.button("Open Notepad"):
        os.system(f"notepad {file}")
elif cmd == "2. Docker Images":
    st.code(os.popen("docker images").read())
elif cmd == "3. Docker PS":
    st.code(os.popen("docker ps -a").read())
elif cmd == "4. Docker Pull":
    image = st.text_input("Image name:")
    if st.button("Pull"):
        st.code(os.popen(f"docker pull {image}").read())
elif cmd == "5. Start Docker Container":
    cname = st.text_input("Container name:")
    if st.button("Start"):
        st.code(os.popen(f"docker start {cname}").read())
elif cmd == "6. Stop Docker Container":
    cname = st.text_input("Container name:")
    if st.button("Stop"):
        st.code(os.popen(f"docker stop {cname}").read())
