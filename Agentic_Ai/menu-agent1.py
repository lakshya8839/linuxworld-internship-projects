from langchain.agents import tool
import subprocess
import platform

# ✅ 18. Yum Config Check (Linux only)
@tool
def yum_check(_: str = "") -> str:
    """
    🔍 Shows Yum configuration (Linux only).
    Equivalent to: `yum repolist all`
    """
    if platform.system() != "Linux":
        return "❌ Yum is only available on Linux."
    try:
        output = subprocess.check_output("yum repolist all", shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Failed to check yum config: {e}"

# ✅ 19. ssh-keygen
@tool
def generate_ssh_key(_: str = "") -> str:
    """
    🔐 Generates an RSA SSH key pair. Manual password entry required.
    Equivalent to: `ssh-keygen -t rsa`
    """
    return "🔐 Please run manually in terminal: ssh-keygen -t rsa"

# ✅ 20. scp file transfer
@tool
def scp_transfer(details: str) -> str:
    """
    🔁 Transfers file using SCP.
    Input format: `source_file user@ip:/path/to/destination`
    Example: `test.txt root@192.168.1.10:/root/`
    """
    try:
        src, dest = details.strip().split()
        subprocess.run(["scp", src, dest], check=True)
        return f"✅ File {src} copied to {dest}"
    except Exception as e:
        return f"❌ Failed to transfer file via scp: {e}"

# ✅ 21. Minikube Setup (Requirements echo)
@tool
def minikube_requirements(_: str = "") -> str:
    """
    📦 Echoes requirements and path needed for Minikube.
    """
    return (
        "🔧 Requirements for Minikube:\n"
        "- Virtualization enabled (VT-x/AMD-V)\n"
        "- Hypervisor (VirtualBox, Docker, Hyper-V)\n"
        "- kubectl\n"
        "- Minikube binary in PATH\n"
        "👉 Check: minikube version"
    )

# ✅ 22. Minikube Start Command
@tool
def start_minikube(_: str = "") -> str:
    """
    🚀 Starts Minikube cluster.
    Equivalent: `minikube start`
    """
    try:
        output = subprocess.check_output("minikube start", shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Failed to start Minikube: {e}"

# ✅ 23. yum install httpd
@tool
def install_apache(_: str = "") -> str:
    """
    🌐 Installs Apache HTTP server using yum (Linux).
    Equivalent: `yum install httpd`
    """
    if platform.system() != "Linux":
        return "❌ Only available on Linux."
    try:
        subprocess.run("sudo yum install httpd", shell=True, check=True)
        return "✅ Apache HTTPD installed."
    except Exception as e:
        return f"❌ Failed to install Apache: {e}"

# ✅ 24. rpm -q httpd
@tool
def check_apache_rpm(_: str = "") -> str:
    """
    📦 Checks if Apache is installed via rpm.
    Equivalent: `rpm -q httpd`
    """
    try:
        output = subprocess.check_output("rpm -q httpd", shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Apache not found: {e}"

# ✅ 25. yum install httpd -y
@tool
def install_apache_auto(_: str = "") -> str:
    """
    🧠 Installs Apache without prompt using yum -y.
    Equivalent: `yum install httpd -y`
    """
    try:
        subprocess.run("sudo yum install httpd -y", shell=True, check=True)
        return "✅ Apache installed with auto confirmation."
    except Exception as e:
        return f"❌ Auto install failed: {e}"

# ✅ 26. systemctl start httpd
@tool
def start_apache(_: str = "") -> str:
    """
    ▶️ Starts Apache HTTP service.
    Equivalent: `systemctl start httpd`
    """
    try:
        subprocess.run("sudo systemctl start httpd", shell=True, check=True)
        return "✅ Apache started."
    except Exception as e:
        return f"❌ Failed to start Apache: {e}"

# ✅ 27. systemctl status httpd
@tool
def status_apache(_: str = "") -> str:
    """
    ℹ️ Checks Apache status.
    Equivalent: `systemctl status httpd`
    """
    try:
        output = subprocess.check_output("sudo systemctl status httpd", shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Could not get status: {e}"

# ✅ 28. systemctl stop firewalld
@tool
def stop_firewalld(_: str = "") -> str:
    """
    🔥 Stops the firewall service.
    Equivalent: `systemctl stop firewalld`
    """
    try:
        subprocess.run("sudo systemctl stop firewalld", shell=True, check=True)
        return "✅ firewalld service stopped."
    except Exception as e:
        return f"❌ Failed to stop firewalld: {e}"

# ✅ 29. systemctl enable httpd
@tool
def enable_apache(_: str = "") -> str:
    """
    🛠️ Enables Apache to start on boot.
    Equivalent: `systemctl enable httpd`
    """
    try:
        subprocess.run("sudo systemctl enable httpd", shell=True, check=True)
        return "✅ Apache enabled on boot."
    except Exception as e:
        return f"❌ Failed to enable Apache: {e}"

# ✅ 30. systemctl restart httpd
@tool
def restart_apache(_: str = "") -> str:
    """
    🔁 Restarts Apache HTTP service.
    Equivalent: `systemctl restart httpd`
    """
    try:
        subprocess.run("sudo systemctl restart httpd", shell=True, check=True)
        return "✅ Apache restarted."
    except Exception as e:
        return f"❌ Failed to restart Apache: {e}"
