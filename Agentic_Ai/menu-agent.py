from langchain.agents import tool
import subprocess
import platform
import os

# ✅ 1. Date Command
@tool
def get_date(_: str = "") -> str:
    """
    📅 Returns the current date using the system date command.
    Automatically detects OS (Linux/Windows) and runs the appropriate command.
    """
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output("date /T", shell=True)
        else:
            output = subprocess.check_output("date", shell=True)
        return output.decode().strip()
    except Exception as e:
        return f"❌ Failed to get date: {e}"

# ✅ 2. Cal Command (Linux only)
@tool
def get_calendar(_: str = "") -> str:
    """
    🗓️ Returns the current calendar using `cal` command (Linux only).
    """
    if platform.system() != "Linux":
        return "❌ The `cal` command is only available on Linux."
    try:
        output = subprocess.check_output("cal", shell=True)
        return output.decode().strip()
    except Exception as e:
        return f"❌ Failed to get calendar: {e}"

# ✅ 3. Ifconfig / ipconfig
@tool
def get_ip_config(_: str = "") -> str:
    """
    🌐 Shows network configuration.
    Uses `ipconfig` on Windows and `ifconfig` or `ip a` on Linux.
    """
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

# ✅ 4. ls / dir
@tool
def list_files(_: str = "") -> str:
    """
    📁 Lists files in the current directory.
    Uses `dir` for Windows and `ls -l` for Linux.
    """
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output("dir", shell=True)
        else:
            output = subprocess.check_output("ls -l", shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Failed to list files: {e}"

# ✅ 5. mkdir
@tool
def make_directory(dir_name: str) -> str:
    """
    📂 Creates a directory with the given name.
    Works on both Windows and Linux.
    """
    try:
        os.makedirs(dir_name, exist_ok=True)
        return f"✅ Directory '{dir_name}' created successfully."
    except Exception as e:
        return f"❌ Failed to create directory: {e}"

# ✅ 6. useradd (Linux only)
@tool
def add_user(username: str) -> str:
    """
    👤 Adds a user to the system (Linux only).
    Requires sudo/root privileges.
    """
    if platform.system() != "Linux":
        return "❌ The `useradd` command is only supported on Linux."
    try:
        subprocess.run(["sudo", "useradd", username], check=True)
        return f"✅ User '{username}' added successfully."
    except Exception as e:
        return f"❌ Failed to add user: {e}"

# ✅ 7. userdel (Linux only)
@tool
def delete_user(username: str) -> str:
    """
    ❌ Deletes a user from the system (Linux only).
    Requires sudo/root privileges.
    """
    if platform.system() != "Linux":
        return "❌ The `userdel` command is only supported on Linux."
    try:
        subprocess.run(["sudo", "userdel", username], check=True)
        return f"✅ User '{username}' deleted successfully."
    except Exception as e:
        return f"❌ Failed to delete user: {e}"

# ✅ 8. List all file permissions
@tool
def list_all_permissions(_: str = "") -> str:
    """
    🔐 Lists all files with permissions in the current directory.
    Uses `ls -l` for Linux/macOS and `icacls` for Windows.
    """
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output("icacls *", shell=True)
        else:
            output = subprocess.check_output("ls -l", shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Failed to list permissions: {e}"

# ✅ 9. Show particular file permissions
@tool
def show_file_permissions(filename: str) -> str:
    """
    🔍 Shows permissions of a specific file.
    Uses `icacls` on Windows and `ls -l` on Linux.
    """
    try:
        if platform.system() == "Windows":
            cmd = f"icacls {filename}"
        else:
            cmd = f"ls -l {filename}"
        output = subprocess.check_output(cmd, shell=True)
        return output.decode(errors="ignore")
    except Exception as e:
        return f"❌ Failed to get file permissions: {e}"

# ✅ 10. Change file permissions
@tool
def change_file_permissions(input_str: str) -> str:
    """
    ✏️ Changes file permissions.
    Input should be '<chmod_value> <filename>' (Linux only).
    Example: '755 test.sh'
    """
    if platform.system() != "Linux":
        return "❌ Changing file permissions is only supported on Linux via chmod."
    try:
        mode, file = input_str.strip().split()
        subprocess.run(["chmod", mode, file], check=True)
        return f"✅ Permissions changed to {mode} for {file}"
    except Exception as e:
        return f"❌ Failed to change permissions: {e}"

# ✅ 11. Create file
@tool
def create_file(filename: str) -> str:
    """
    📄 Creates a blank file with the given name.
    Works cross-platform.
    """
    try:
        open(filename, 'a').close()
        return f"✅ File '{filename}' created successfully."
    except Exception as e:
        return f"❌ Failed to create file: {e}"

# ✅ 12. Change Directory (cd)
@tool
def change_directory(dir_name: str) -> str:
    """
    📁 Changes the current working directory to the specified one.
    """
    try:
        os.chdir(dir_name)
        return f"✅ Changed directory to: {os.getcwd()}"
    except Exception as e:
        return f"❌ Failed to change directory: {e}"

# ✅ 13. Change user (Linux only)
@tool
def switch_user(username: str) -> str:
    """
    👤 Switches to another user account using `su`.
    Only supported in Linux. Requires password entry.
    """
    if platform.system() != "Linux":
        return "❌ `su` command is Linux-only."
    return f"🔒 Please run this command manually in terminal: su - {username}"

# ✅ 14. pip install
@tool
def pip_install(lib: str) -> str:
    """
    📦 Installs a Python library using pip.
    Works in current Python environment.
    """
    try:
        subprocess.run(["pip", "install", lib], check=True)
        return f"✅ Installed Python library: {lib}"
    except Exception as e:
        return f"❌ Failed to install {lib}: {e}"

# ✅ 15. Open Notepad (Windows only)
@tool
def open_notepad(file: str) -> str:
    """
    📝 Opens a file in Notepad (Windows only).
    """
    if platform.system() != "Windows":
        return "❌ Notepad is only available on Windows."
    try:
        subprocess.Popen(["notepad", file])
        return f"✅ Opening '{file}' in Notepad..."
    except Exception as e:
        return f"❌ Failed to open Notepad: {e}"

# ✅ 16. Open gedit (Linux only)
@tool
def open_gedit(file: str) -> str:
    """
    📝 Opens a file in gedit (Linux GUI text editor).
    """
    if platform.system() != "Linux":
        return "❌ gedit is only available on Linux."
    try:
        subprocess.Popen(["gedit", file])
        return f"✅ Opening '{file}' in gedit..."
    except Exception as e:
        return f"❌ Failed to open gedit: {e}"

# ✅ 17. Open vim (Linux only)
@tool
def open_vim(file: str) -> str:
    """
    ⌨️ Opens a file in Vim (Linux CLI editor).
    """
    if platform.system() != "Linux":
        return "❌ Vim is only available on Linux."
    return f"📝 Run manually in terminal: vim {file}"

# Next tools: yum config, ssh-keygen, scp, minikube, docker, etc.
# Let me know to continue with 18–30 or batch of your choice.
