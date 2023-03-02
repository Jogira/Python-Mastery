from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path
from string  import Template

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"] = "Zweitonegoismus@gmail.com"
message["subject"] = "Test"

body = template.substitute({"name": "Zwei"})

message.attach(MIMEText(body, "html"))
# message.attach(MIMEImage(Path("Zwei.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email@gmail.com", "pass12345~~")
    smtp.send_message(message)
    print("Sent...")