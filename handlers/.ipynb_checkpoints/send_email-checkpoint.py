#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# handlers/send_email.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

class SendEmailHandler:
    def __init__(self, context=None):
        self.context = context

    def handle(self, plan):
        recipient = plan.get("recipient")
        subject = plan.get("subject", "VoiceFlow Agent Email")
        body = plan.get("body", "This is a message sent by your AI assistant.")

        if not recipient:
            print(" No recipient specified.")
            return

        try:
            self.send_email(recipient, subject, body)
            print(f"📧 Email sent to {recipient}!")
        except Exception as e:
            print(f" Failed to send email: {e}")

    def send_email(self, to_email, subject, body):
        # Read from .env
        smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = int(os.getenv("SMTP_PORT", 587))
        sender_email = os.getenv("EMAIL_ADDRESS")
        sender_password = os.getenv("EMAIL_PASSWORD")

        if not sender_email or not sender_password:
            raise ValueError("Missing sender credentials in .env")

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

