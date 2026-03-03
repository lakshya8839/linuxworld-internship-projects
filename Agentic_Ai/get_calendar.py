from langchain.agents import tool
import subprocess
import platform

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