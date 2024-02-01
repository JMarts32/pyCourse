import smtplib
import getpass
import email
import sched
import os

HOST = "smtp-mail.hotmail.com"
PORT = 587

FROM = input("Enter the email you are sending the emails: ")
TO_EMAIL = []
PASSWORD = getpass.getpass("Enter the password: ")

MESSAGE = ""

smtp = smtplib.SMTP(HOST, PORT)
statuscode, response = smtp.ehlo()
# Echo the server

tls_statuscode, tls_reponse = smtp.starttls()
# establishing the tls connection

login_statuscode, login_repsonse = smtp.login(FROM, PASSWORD)
# Login into the emial

smtp.sendmail(FROM, TO_EMAIL, MESSAGE)
smtp.quit()