# https://ethereal.email/create
# html_body = "<h1>Hello!</h1><p>এটা <b>বোল্ড</b> লেখা</p>"
# message.attach(MIMEText(html_body, "html"))

import smtplib # smtplib- simple mail transfer protocol
from email.mime.multipart import MIMEMultipart # Used for creating an empty kham (header)
from email.mime.text import MIMEText # Used for creating body

sender_email = "dale13@ethereal.email"
sender_password = "9V2tHHmfdENjP7trXu"
receiver_email = "Afnan@gmail.com"
subject = "Automated email test"
body = "Hello, I am your chatbot"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Cc"] = "hjdkkha@gmail.com"


message.attach(MIMEText(body, "plain")) # Attaches header + body; HTML can also be added by replacing plain with html and body with html_body
server = smtplib.SMTP("smtp.ethereal.email", 587) # Connect to mail server. Here 587 is port number (specific door number)
server.starttls() # ensures data security, tls- transport layer security

server.login(sender_email, sender_password)
server.sendmail(sender_email, receiver_email, message.as_string())
print("Email sent")
server.quit()