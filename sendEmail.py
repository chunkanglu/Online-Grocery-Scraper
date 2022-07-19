from email.message import EmailMessage
import smtplib

HOST_ADDRESS = "smtp-mail.outlook.com"
PORT = 587

def sendEmail(_from, _to, filename, subject, pwd):
    msg = EmailMessage()
    msg["From"] = _from
    msg["Subject"] = subject
    msg["To"] = _to
    # msg.set_content("Attached is the price data.")
    msg.add_attachment(open(filename, "r").read(), filename=filename)

    server = smtplib.SMTP(HOST_ADDRESS, PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(_from, pwd)

    server.send_message(msg)