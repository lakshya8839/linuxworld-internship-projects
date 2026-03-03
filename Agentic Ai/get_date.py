from langchain.agents import tool
import subprocess
import platform

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