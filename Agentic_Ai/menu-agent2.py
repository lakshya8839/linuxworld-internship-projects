from langchain.agents import tool
import os

# ✅ 31. Instagram Single Post
@tool
def insta_single_post(_: str = "") -> str:
    """
    📸 Uploads a single image post to Instagram.
    Requires instagrapi configured and user credentials via secure method.
    """
    return "🔒 This tool requires login credentials and media file path. Please implement securely with instagrapi."

# ✅ 32. Instagram Multi Image Post
@tool
def insta_multi_post(_: str = "") -> str:
    """
    🖼️ Uploads multiple images to Instagram as a carousel post.
    Requires valid login and list of image paths.
    """
    return "🔒 This tool requires login credentials and list of image paths. Please implement securely with instagrapi."

# ✅ 33. Send Email
@tool
def send_email(_: str = "") -> str:
    """
    📧 Sends an email.
    This tool requires secure SMTP setup. Use `smtplib` with `email.mime`.
    """
    return "🔒 Requires sender, receiver, subject, and message setup using smtplib."

# ✅ 34. Voice Call (Twilio)
@tool
def voice_call(_: str = "") -> str:
    """
    📞 Makes a voice call using Twilio API.
    Requires Twilio SID, auth token, from and to numbers.
    """
    return "🔒 Setup with Twilio credentials needed. Use `twilio.rest.Client`."

# ✅ 35. Read Tweet Comments
@tool
def read_tweet_comments(_: str = "") -> str:
    """
    🐦 Scrapes replies to a tweet using Selenium.
    Requires ChromeDriver and login to access tweets reliably.
    """
    return "🔒 This requires Selenium setup with Twitter login and target tweet URL."

# Next up: Web scraping and Docker tools.
# Let me know when ready to continue.
