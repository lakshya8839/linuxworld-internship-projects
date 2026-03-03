import os
import getpass

ssh_user = input("Enter SSH username: ")
ssh_ip = input("Enter remote IP: ")

print(
    """
    ---------------------------------------------------
    Linux + Docker Menu Based Project (SSH & Local)
    ---------------------------------------------------
    SSH-Based Commands
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
    15. gedit
    16. vim editor (CLI editor)
    17. Yum Config
    18. ssh-keygen -t rsa
    19. scp file transfer
    20. Minikube Setup (echo requirement + path)
    21. Minikube Start Command
    22. yum install httpd (Apache server)
    23. rpm -q httpd (Check Apache installation)
    24. yum install httpd -y (Auto setup Apache)
    25. systemctl start httpd (Start Apache)
    26. systemctl status httpd (Check Apache status)
    27. systemctl stop firewalld (Stop firewall)
    28. systemctl enable httpd (Enable Apache on boot)
    29. systemctl restart httpd (Restart Apache)
    30. Launch Docker Container (Remote via SSH)
    31. Start Docker Container (Remote via SSH)
    32. Stop Docker Container (Remote via SSH)
    33. Remove Docker Container (Remote via SSH)
    34. List Docker Images (Remote via SSH)
    35. List All Containers (Remote via SSH)
    36. Pull Docker Image (Remote via SSH)
    ---------------------------------------------------
    Local / Windows-Based Commands
    ---------------------------------------------------
    37. Launch Docker Container (Local)
    38. Start Docker Container (Local)
    39. Stop Docker Container (Local)
    40. Remove Docker Container (Local)
    41. List Docker Images (Local)
    42. List All Containers (Local)
    43. Pull Docker Image (Local)
    44. Instagram Single Post
    45. Instagram Multi Image Post
    46. Send Email
    47. Voice Call (Twilio)
    48. Read Tweet Comments
    49. Web Scrape a Website
    50. Open Notepad file (Windows)
    51. Exit
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
        file = input("Enter filename to open with gedit: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} gedit {file}")
    elif choice == "16":
        f = input("Enter file to open with vim: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} vim {f}")
    elif choice == "17":
        os.system(f"ssh {ssh_user}@{ssh_ip} yum-config-manager")
    elif choice == "18":
        k = input("Enter SSH key filename: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} ssh-keygen -t rsa -f ~/.ssh/{k}")
    elif choice == "19":
        s = input("Source file path: ")
        d = input("Destination user@ip:/path/: ")
        os.system(f"scp {s} {d}")
    elif choice == "20":
        os.system(f"ssh {ssh_user}@{ssh_ip} 'echo Set environment variable and Minikube path'")
    elif choice == "21":
        os.system(f"ssh {ssh_user}@{ssh_ip} minikube start")
    elif choice == "22":
        os.system(f"ssh {ssh_user}@{ssh_ip} yum install httpd")
    elif choice == "23":
        os.system(f"ssh {ssh_user}@{ssh_ip} rpm -q httpd")
    elif choice == "24":
        os.system(f"ssh {ssh_user}@{ssh_ip} yum install httpd -y")
    elif choice == "25":
        os.system(f"ssh {ssh_user}@{ssh_ip} systemctl start httpd")
    elif choice == "26":
        os.system(f"ssh {ssh_user}@{ssh_ip} systemctl status httpd")
    elif choice == "27":
        os.system(f"ssh {ssh_user}@{ssh_ip} systemctl stop firewalld")
    elif choice == "28":
        os.system(f"ssh {ssh_user}@{ssh_ip} systemctl enable httpd")
    elif choice == "29":
        os.system(f"ssh {ssh_user}@{ssh_ip} systemctl restart httpd")
    elif choice == "30":
        name = input("Container name: ")
        image = input("Image name: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} docker run -dit --name {name} {image}")
    elif choice == "31":
        name = input("Container name: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} docker start {name}")
    elif choice == "32":
        name = input("Container name: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} docker stop {name}")
    elif choice == "33":
        name = input("Container name: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} docker rm {name}")
    elif choice == "34":
        os.system(f"ssh {ssh_user}@{ssh_ip} docker images")
    elif choice == "35":
        os.system(f"ssh {ssh_user}@{ssh_ip} docker ps -a")
    elif choice == "36":
        image = input("Enter image name: ")
        os.system(f"ssh {ssh_user}@{ssh_ip} docker pull {image}")
    elif choice == "37":
        name = input("Container name: ")
        image = input("Image name: ")
        os.system(f"docker run -dit --name {name} {image}")
    elif choice == "38":
        name = input("Container name: ")
        os.system(f"docker start {name}")
    elif choice == "39":
        name = input("Container name: ")
        os.system(f"docker stop {name}")
    elif choice == "40":
        name = input("Container name: ")
        os.system(f"docker rm {name}")
    elif choice == "41":
        os.system("docker images")
    elif choice == "42":
        os.system("docker ps -a")
    elif choice == "43":
        image = input("Enter image name: ")
        os.system(f"docker pull {image}")
    elif choice == "44":
        from instagrapi import Client
        cl = Client()
        u = input("Instagram username: ")
        p = getpass.getpass("Instagram password: ")
        cl.login(u, p)
        img = input("Image path: ")
        caption = input("Caption: ")
        cl.photo_upload(path=img, caption=caption)
    elif choice == "45":
        from instagrapi import Client
        cl = Client()
        u = input("Instagram username: ")
        p = getpass.getpass("Instagram password: ")
        cl.login(u, p)
        count = int(input("Number of images: "))
        imgs = [input(f"Image {i+1}: ") for i in range(count)]
        caption = input("Caption: ")
        cl.album_upload(paths=imgs, caption=caption)
    elif choice == "46":
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
    elif choice == "47":
        from twilio.rest import Client as TwilioClient
        sid = input("Twilio SID: ")
        token = getpass.getpass("Twilio Token: ")
        from_no = input("From number: ")
        to_no = input("To number: ")
        client = TwilioClient(sid, token)
        call = client.calls.create(
            twiml='<Response><Say>Hello from Python</Say></Response>',
            to=to_no,
            from_=from_no
        )
        print("Call SID:", call.sid)
    elif choice == "48":
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        import time, random
        url = input("Enter Tweet URL: ")
        win_user = input("Enter Windows username: ")
        options = Options()
        options.add_argument(f"user-data-dir=C:/Users/{win_user}/AppData/Local/Google/Chrome/User Data")
        options.add_argument("--profile-directory=Default")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        time.sleep(5)
        for _ in range(5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(2, 4))
        articles = driver.find_elements(By.XPATH, "//article")
        replies = [a.text for a in articles if a.text.strip()]
        with open("replies.txt", "w", encoding="utf-8") as f:
            for r in replies:
                f.write(r + "\n\n")
        driver.quit()
    elif choice == "49":
        import requests
        from bs4 import BeautifulSoup
        url = input("Enter URL: ")
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        headings = soup.find_all(['h1','h2','h3','h4','h5','h6'])
        paragraphs = soup.find_all('p')
        print("\nHeadings:")
        for tag in headings:
            print(tag.text.strip())
        print("\nParagraphs:")
        for p in paragraphs:
            print(p.text.strip())
    elif choice == "50":
        f = input("File to open in notepad: ")
        os.system(f"notepad {f}")
    elif choice == "51":
        break
    else:
        print("Invalid option.")
