import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "sender mail @gmail.com"
receiver_email = "receiver mail @gmail.com"
password = "Add your 2-step verification password(get generated 16 digit password from google account)"  # App Password recommended!

# Create email content (HTML + plain text)
message = MIMEMultipart("alternative")
message["Subject"] = "Test Email from Python"
message["From"] = sender_email
message["To"] = receiver_email

text = "This is the plain text version of the email."
html = """
<html>
  <body>
    <h2>Hello!</h2>
    <p>This is a <b>HTML</b> email sent from Python.</p>
  </body>
</html>
"""

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

# Send email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
except Exception as e:
    print("Error:", e)
