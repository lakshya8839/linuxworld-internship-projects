import os
import getpass

ssh_user = input("Enter SSH username: ")
ssh_ip = input("Enter remote IP: ")

print(
    """
    ---------------------------------------------------
    Linux + Docker Menu Based Project (SSH & Local)
    ---------------------------------------------------
    1. Date Command
    2. Cal command
    3. Ifconfig command
    4. ls command
    5. mkdir command
    6. useradd command
    7. userdel command
    8. list all file permissions
    9. show particular file permissions
    10. Change file permissions
    11. Create file
    12. Change Directory (cd)
    13. Change user (sudo user)
    14. pip install (library)
    15. Open notepad file
    16. gedit
    17. vim editor (CLI editor)
    18. Yum Config
    19. ssh-keygen -t rsa
    20. scp file transfer
    21. Minikube Setup (echo requirement + path)
    22. Minikube Start Command
    23. yum install httpd (Apache server)
    24. rpm -q httpd (Check Apache installation)
    25. yum install httpd -y (Auto setup Apache)
    26. systemctl start httpd (Start Apache)
    27. systemctl status httpd (Check Apache status)
    28. systemctl stop firewalld (Stop firewall)
    29. systemctl enable httpd (Enable Apache on boot)
    30. systemctl restart httpd (Restart Apache)
    31. Instagram Single Post
    32. Instagram Multi Image Post
    33. Send Email
    34. Voice Call (Twilio)
    35. Read Tweet Comments
    36. Web Scrape a Website (Headings and Paragraphs)
    37. Launch Docker Container (Remote via SSH)
    38. Start Docker Container (Remote via SSH)
    39. Stop Docker Container (Remote via SSH)
    40. Remove Docker Container (Remote via SSH)
    41. List Docker Images (Remote via SSH)
    42. List All Containers (Remote via SSH)
    43. Pull Docker Image (Remote via SSH)
    44. Launch Docker Container (Local)
    45. Start Docker Container (Local)
    46. Stop Docker Container (Local)
    47. Remove Docker Container (Local)
    48. List Docker Images (Local)
    49. List All Containers (Local)
    50. Pull Docker Image (Local)
    51. Return to Main Menu
    52. Exit
    """
)

while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        os.system(f"ssh {ssh_user}@{ssh_ip} date")
    elif choice == "2":
        os.system(f"ssh {ssh_user}@{ssh_ip} cal")
    elif choice == "3":
        os.system(f"ssh {ssh_user}@{ssh_ip} ifconfig")
    elif choice == "4":
        os.system(f"ssh {ssh_user}@{ssh_ip} ls")
    elif choice == "5":
        d = input("Enter new directory name: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} mkdir {d}")
    elif choice == "6":
        u = input("Enter username to add: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} useradd {u}")
    elif choice == "7":
        u = input("Enter username to delete: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} userdel {u}")
    elif choice == "8":
        os.system(f"ssh {ssh_user}@{ssh_ip} ls -l")
    elif choice == "9":
        f = input("Enter file name: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} ls -l {f}")
    elif choice == "10":
        f = input("File name: ")
        who = input("User(u)/Group(g)/Other(o): ")
        mod = input("Add(+)/Remove(-): ")
        perms = input("Permission (r/w/x): ")
        os.system(f"ssh {ssh_user}@{ssh_ip} chmod {who}{mod}{perms} {f}")
    elif choice == "11":
        f = input("Enter file name to create: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} touch {f}")
    elif choice == "12":
        path = input("Enter path to cd: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} cd {path} && pwd")
    elif choice == "13":
        sudo_user = input("Enter user to sudo into: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} sudo su - {sudo_user}")
    elif choice == "14":
        lib = input("Enter pip package to install: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} pip install {lib}")
    elif choice == "15":
        f = input("Enter file to open with notepad: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} notepad {f}")
    elif choice == "16":
        os.system(f"ssh {ssh_user}@{ssh_ip} gedit")
    elif choice == "17":
        f = input("Enter file to open with vim: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} vim {f}")
    elif choice == "18":
        os.system(f"ssh {ssh_user}@{ssh_ip} yum-config-manager")
    elif choice == "19":
        k = input("Enter SSH key filename: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} ssh-keygen -t rsa -f ~/.ssh/{k}")
    elif choice == "20":
        s = input("Source file path: ")
        d = input("Destination user@ip:/path/: ")
        os.system(f"scp {s} {d}")
    elif choice == "21":
        os.system(f"ssh {ssh_user}@{ssh_ip} 'echo Set environment variable and Minikube path'")
    elif choice == "22":
        os.system(f"ssh {ssh_user}@{ssh_ip} minikube start")
    elif choice == "23":
        os.system(f"ssh {ssh_user}@{ssh_ip} yum install httpd")
    elif choice == "24":
        os.system(f"ssh {ssh_user}@{ssh_ip} rpm -q httpd")
    elif choice == "25":
        os.system(f"ssh {ssh_user}@{ssh_ip} yum install httpd -y")
    elif choice == "26":
        os.system(f"ssh {ssh_user}@{ssh_ip} systemctl start httpd")
    elif choice == "27":
        os.system(f"ssh {ssh_user}@{ssh_ip} systemctl status httpd")
    elif choice == "28":
        os.system(f"ssh {ssh_user}@{ssh_ip} systemctl stop firewalld")
    elif choice == "29":
        os.system(f"ssh {ssh_user}@{ssh_ip} systemctl enable httpd")
    elif choice == "30":
        os.system(f"ssh {ssh_user}@{ssh_ip} systemctl restart httpd")
    elif choice == "31":
        from instagrapi import Client
        cl = Client()
        insta_user = input("Enter Instagram username: ")
        insta_pass = getpass.getpass("Enter Instagram password: ")
        cl.login(insta_user, insta_pass)
        img_path = input("Enter path to image: ")
        caption = input("Enter caption: ")
        cl.photo_upload(path=img_path, caption=caption)
    elif choice == "32":
        from instagrapi import Client
        cl = Client()
        insta_user = input("Enter Instagram username: ")
        insta_pass = getpass.getpass("Enter Instagram password: ")
        cl.login(insta_user, insta_pass)
        paths = []
        count = int(input("Number of images: "))
        for i in range(count):
            paths.append(input(f"Image {i+1} path: "))
        caption = input("Enter caption: ")
        media = cl.album_upload(paths=paths, caption=caption)
        print("Uploaded:", media.dict())
    elif choice == "33":
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        sender = input("Sender email: ")
        receiver = input("Receiver email: ")
        password = getpass.getpass("App password: ")
        subject = input("Subject: ")
        text = input("Plain text: ")
        html = input("HTML content: ")

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver
        msg.attach(MIMEText(text, "plain"))
        msg.attach(MIMEText(html, "html"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("Email sent successfully.")
    elif choice == "34":
        from twilio.rest import Client as TwilioClient
        sid = input("Twilio SID: ")
        token = getpass.getpass("Twilio Token: ")
        from_no = input("Twilio From No (+countrycode): ")
        to_no = input("Recipient No (+countrycode): ")

        twilio_client = TwilioClient(sid, token)
        call = twilio_client.calls.create(
            twiml='<Response><Say voice="alice" language="en-IN">Hello, this is an automated call. Have a great day!</Say></Response>',
            to=to_no,
            from_=from_no
        )
        print("Call SID:", call.sid)
    elif choice == "35":
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        import time
        import random

        tweet_url = input("Enter Tweet URL: ")
        chrome_user = input("Enter your Windows username: ")

        options = Options()
        options.add_argument(f"user-data-dir=C:/Users/{chrome_user}/AppData/Local/Google/Chrome/User Data")
        options.add_argument("--profile-directory=Default")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        try:
            driver.get(tweet_url)
            time.sleep(5)
            for _ in range(10):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.uniform(3, 5))
            articles = driver.find_elements(By.XPATH, "//article")
            replies = []
            for article in articles[1:]:
                try:
                    text = article.text.strip()
                    if text and text not in replies:
                        replies.append(text)
                except:
                    continue
            with open("replies.txt", "w", encoding="utf-8") as f:
                for reply in replies:
                    f.write(reply + "\n\n")
            print(len(replies), "replies saved.")
        finally:
            driver.quit()
    elif choice == "36":
        import requests
        from bs4 import BeautifulSoup

        url = input("Enter the URL to scrape: ")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        paragraphs = soup.find_all('p')

        print("\nHeadings:")
        for tag in headings:
            text = tag.text.strip()
            if text:
                print(text)

        print("\nParagraphs:")
        for p in paragraphs:
            text = p.text.strip()
            if text:
                print(text)
    elif choice == "37":
        name = input("Enter container name: ")
        image = input("Enter image name: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} docker run -dit --name {name} {image}")
    elif choice == "38":
        name = input("Enter container name: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} docker start {name}")
    elif choice == "39":
        name = input("Enter container name: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} docker stop {name}")
    elif choice == "40":
        name = input("Enter container name: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} docker rm {name}")
    elif choice == "41":
        os.system(f"ssh {ssh_user}@{ssh_ip} docker images")
    elif choice == "42":
        os.system(f"ssh {ssh_user}@{ssh_ip} docker ps -a")
    elif choice == "43":
        image = input("Enter image name: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} docker pull {image}")
    elif choice == "44":
        name = input("Enter container name: ")
        image = input("Enter image name: ")
        os.system(f"docker run -dit --name {name} {image}")
    elif choice == "45":
        name = input("Enter container name: ")
        os.system(f"docker start {name}")
    elif choice == "46":
        name = input("Enter container name: ")
        os.system(f"docker stop {name}")
    elif choice == "47":
        name = input("Enter container name: ")
        os.system(f"docker rm {name}")
    elif choice == "48":
        os.system("docker images")
    elif choice == "49":
        os.system("docker ps -a")
    elif choice == "50":
        image = input("Enter image name: ")
        os.system(f"docker pull {image}")
    elif choice == "51":
        print("Returning to main menu...")
    elif choice == "52":
        break
    else:
        print("Invalid option.")
