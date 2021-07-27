
import re

import os
import datetime
import smtplib

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
# // defining a function which will be sending emails
def send_mail(reciever_mail_address, name):
  sender_mail_address = "luigi_tabarca@yahoo.ro"
  passwd = "oswechrrqstbtnok"
#   //connecting to gmail server with domain name and port number
  obj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
  obj.ehlo()
  obj.starttls()
#   // logging into your gmail account
  obj.login(sender_mail_address, passwd)
#   // sending mail to ‘reciever_mail_address’.
  text=create_message()
  obj.sendmail(sender_mail_address, reciever_mail_address, text)

#   // ending connection
  obj.quit()

def create_message():
    message = MIMEMultipart()
    message["From"] = "luigi_tabarca@yahoo.ro"
    message["To"] ="luigitabarca88@gmail.com"
    message["Subject"] = "Raport cantariri"
    # message["Bcc"] = receiver_email  # Recommended for mass emails
    body = "This is an email with attachment sent from Python"
    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "font-colors.pdf"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    return message.as_string()

send_mail("luigitabarca88@gmail.com", "name")