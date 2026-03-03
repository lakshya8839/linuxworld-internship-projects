from langchain.agents import tool
import subprocess
import os
import platform

# ✅ 36. Web Scrape (Headings + Paragraphs)
from bs4 import BeautifulSoup
import requests

@tool
def scrape_website(url: str) -> str:
    """
    🌐 Scrapes headings (h1–h3) and paragraphs from a given website URL.
    """
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        data = ""
        for tag in soup.find_all(['h1', 'h2', 'h3', 'p']):
            data += f"{tag.name.upper()}: {tag.text.strip()}\n"
        return data[:4000] or "No content found."
    except Exception as e:
        return f"❌ Failed to scrape website: {e}"

# ✅ SSH Helper
import paramiko

def ssh_exec(ip, user, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=user, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode() + stderr.read().decode()
        ssh.close()
        return output.strip()
    except Exception as e:
        return f"❌ SSH Error: {e}"

# ✅ 37–43: Docker (Remote via SSH)

@tool
def remote_docker_launch(details: str) -> str:
    """
    🚀 Launches a Docker container remotely.
    Input format: '<user> <ip> <password> <image_name>'
    """
    try:
        user, ip, pwd, image = details.strip().split()
        cmd = f"docker run -dit --name auto_{image.replace(':', '_')} {image}"
        return ssh_exec(ip, user, pwd, cmd)
    except Exception as e:
        return f"❌ Failed: {e}"

@tool
def remote_docker_start(details: str) -> str:
    """
    ▶️ Start existing Docker container (Remote).
    Input format: '<user> <ip> <password> <container>'
    """
    try:
        user, ip, pwd, name = details.strip().split()
        return ssh_exec(ip, user, pwd, f"docker start {name}")
    except Exception as e:
        return f"❌ Failed: {e}"

@tool
def remote_docker_stop(details: str) -> str:
    """
    ⏹️ Stop running Docker container (Remote).
    Input format: '<user> <ip> <password> <container>'
    """
    try:
        user, ip, pwd, name = details.strip().split()
        return ssh_exec(ip, user, pwd, f"docker stop {name}")
    except Exception as e:
        return f"❌ Failed: {e}"

@tool
def remote_docker_remove(details: str) -> str:
    """
    ❌ Remove Docker container (Remote).
    Input format: '<user> <ip> <password> <container>'
    """
    try:
        user, ip, pwd, name = details.strip().split()
        return ssh_exec(ip, user, pwd, f"docker rm {name}")
    except Exception as e:
        return f"❌ Failed: {e}"

@tool
def remote_docker_images(details: str) -> str:
    """
    🧱 List all Docker images (Remote).
    Input format: '<user> <ip> <password>'
    """
    try:
        user, ip, pwd = details.strip().split()
        return ssh_exec(ip, user, pwd, "docker images")
    except Exception as e:
        return f"❌ Failed: {e}"

@tool
def remote_docker_ps(details: str) -> str:
    """
    📦 List all containers (Remote).
    Input format: '<user> <ip> <password>'
    """
    try:
        user, ip, pwd = details.strip().split()
        return ssh_exec(ip, user, pwd, "docker ps -a")
    except Exception as e:
        return f"❌ Failed: {e}"

@tool
def remote_docker_pull(details: str) -> str:
    """
    📥 Pull a Docker image (Remote).
    Input format: '<user> <ip> <password> <image>'
    """
    try:
        user, ip, pwd, image = details.strip().split()
        return ssh_exec(ip, user, pwd, f"docker pull {image}")
    except Exception as e:
        return f"❌ Failed: {e}"

# ✅ 44–50: Local Docker

def local_run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode(errors="ignore")
    except Exception as e:
        return f"❌ Failed: {e}"

@tool
def local_docker_launch(image: str) -> str:
    """
    🚀 Launch a Docker container (Local).
    """
    return local_run(f"docker run -dit --name auto_{image.replace(':','_')} {image}")

@tool
def local_docker_start(container: str) -> str:
    """
    ▶️ Start container (Local).
    """
    return local_run(f"docker start {container}")

@tool
def local_docker_stop(container: str) -> str:
    """
    ⏹️ Stop container (Local).
    """
    return local_run(f"docker stop {container}")

@tool
def local_docker_remove(container: str) -> str:
    """
    ❌ Remove container (Local).
    """
    return local_run(f"docker rm {container}")

@tool
def local_docker_images(_: str = "") -> str:
    """
    🧱 List Docker images (Local).
    """
    return local_run("docker images")

@tool
def local_docker_ps(_: str = "") -> str:
    """
    📦 List all Docker containers (Local).
    """
    return local_run("docker ps -a")

@tool
def local_docker_pull(image: str) -> str:
    """
    📥 Pull a Docker image (Local).
    """
    return local_run(f"docker pull {image}")

# ✅ 51. Return to main menu
@tool
def return_to_main(_: str = "") -> str:
    """
    ⬅️ Return to the main menu.
    """
    return "🔁 Returning to main menu..."