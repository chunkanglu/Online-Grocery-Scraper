from email.message import EmailMessage
import smtplib
import os

def sendEmail():
    msg = EmailMessage()
    msg["From"] = os.environ['EMAIL_FROM']
    msg["Subject"] = os.environ['EMAIL_SUBJECT']
    msg["To"] = os.environ['EMAIL_TO']
    msg.set_content("Attached is the price data.")
    msg.add_attachment(open(os.environ['OUTPUT_FILE_NAME']+".csv", "r").read(), filename=os.environ['OUTPUT_FILE_NAME']+".csv")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(os.environ['EMAIL_FROM'], os.environ['EMAIL_PWD'])

    server.send_message(msg)