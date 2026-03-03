from langchain.agents import tool
import subprocess
import os

# ✅ 36. Web Scrape a Website (Headings and Paragraphs)
@tool
def scrape_headings_paragraphs(url: str) -> str:
    """
    🌐 Scrapes all headings and paragraphs from a URL using BeautifulSoup.
    Format: <url>
    """
    try:
        from bs4 import BeautifulSoup
        import requests
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        headings = "\n".join([h.get_text(strip=True) for h in soup.find_all(['h1','h2','h3'])])
        paragraphs = "\n".join([p.get_text(strip=True) for p in soup.find_all('p')])
        return f"📑 Headings:\n{headings}\n\n📄 Paragraphs:\n{paragraphs}"
    except Exception as e:
        return f"❌ Failed to scrape: {e}"

# ✅ 37. Launch Docker Container (Remote via SSH)
@tool
def ssh_docker_run(params: str) -> str:
    """
    🐳 Launches a Docker container on a remote SSH server.
    Format: <ssh_user>@<ip> <image_name> <container_name>
    """
    try:
        ssh_user_ip, image, cname = params.strip().split()
        cmd = f"ssh {ssh_user_ip} docker run -dit --name {cname} {image}"
        subprocess.run(cmd, shell=True, check=True)
        return f"✅ Docker container '{cname}' launched remotely."
    except Exception as e:
        return f"❌ Failed to launch remote container: {e}"

# ✅ 38. Start Docker Container (Remote via SSH)
@tool
def ssh_docker_start(params: str) -> str:
    """
    ▶️ Starts a Docker container on a remote SSH server.
    Format: <ssh_user>@<ip> <container_name>
    """
    try:
        ssh_user_ip, cname = params.strip().split()
        cmd = f"ssh {ssh_user_ip} docker start {cname}"
        subprocess.run(cmd, shell=True, check=True)
        return f"✅ Container '{cname}' started remotely."
    except Exception as e:
        return f"❌ Failed to start container: {e}"

# ✅ 39. Stop Docker Container (Remote via SSH)
@tool
def ssh_docker_stop(params: str) -> str:
    """
    ⏹️ Stops a Docker container on a remote SSH server.
    Format: <ssh_user>@<ip> <container_name>
    """
    try:
        ssh_user_ip, cname = params.strip().split()
        cmd = f"ssh {ssh_user_ip} docker stop {cname}"
        subprocess.run(cmd, shell=True, check=True)
        return f"✅ Container '{cname}' stopped remotely."
    except Exception as e:
        return f"❌ Failed to stop container: {e}"

# ✅ 40. Remove Docker Container (Remote via SSH)
@tool
def ssh_docker_rm(params: str) -> str:
    """
    🗑️ Removes a Docker container from remote SSH server.
    Format: <ssh_user>@<ip> <container_name>
    """
    try:
        ssh_user_ip, cname = params.strip().split()
        cmd = f"ssh {ssh_user_ip} docker rm {cname}"
        subprocess.run(cmd, shell=True, check=True)
        return f"✅ Container '{cname}' removed remotely."
    except Exception as e:
        return f"❌ Failed to remove container: {e}"

# ✅ 41. List Docker Images (Remote via SSH)
@tool
def ssh_list_docker_images(ssh_target: str) -> str:
    """
    🖼️ Lists Docker images on a remote server via SSH.
    Format: <ssh_user>@<ip>
    """
    try:
        cmd = f"ssh {ssh_target} docker images"
        output = subprocess.check_output(cmd, shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Failed to list images: {e}"

# ✅ 42. List All Containers (Remote via SSH)
@tool
def ssh_list_docker_containers(ssh_target: str) -> str:
    """
    📋 Lists all Docker containers on a remote SSH server.
    Format: <ssh_user>@<ip>
    """
    try:
        cmd = f"ssh {ssh_target} docker ps -a"
        output = subprocess.check_output(cmd, shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Failed to list containers: {e}"

# ✅ 43. Pull Docker Image (Remote via SSH)
@tool
def ssh_docker_pull(params: str) -> str:
    """
    📥 Pulls a Docker image on a remote server.
    Format: <ssh_user>@<ip> <image_name>
    """
    try:
        ssh_user_ip, image = params.strip().split()
        cmd = f"ssh {ssh_user_ip} docker pull {image}"
        subprocess.run(cmd, shell=True, check=True)
        return f"✅ Image '{image}' pulled remotely."
    except Exception as e:
        return f"❌ Failed to pull image: {e}"

# Let me know to continue with 44–50 (Local Docker) and 51 (Return to Main Menu).
