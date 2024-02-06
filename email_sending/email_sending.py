from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date, timedelta
import smtplib
import getpass
import sched


def snd_mail():
    HOST = "smtp-mail.outlook.com"
    PORT = 587

    print("Please make sure that the email is from microsoft :D")
    FROM = input("Enter the email where you are sending the emails: ")
    TO_EMAIL = ["jm2002.santosa@gmail.com"]
    PASSWORD = getpass.getpass("Enter the password: ")

    SUBJECT = "Test Subject"
    BODY = "Hola Juan"

    # Open the logs file and write the day of the session
    logs = open("./logs/logs.txt", "a")
    logday = "Logs from session" + str(date.today()) + "\n"
    logs.write(logday)

    # Estbalishes the connection with the smtp server
    smtp = smtplib.SMTP(HOST, PORT)
    # Echo the server
    statuscode, response = smtp.ehlo()
    logs.write(str(statuscode) + "\n")
    logs.write(str(response) + "\n")
    # establishing the tls connection
    tls_statuscode, tls_reponse = smtp.starttls()
    logs.write(str(tls_statuscode) + "\n")
    logs.write(str(tls_reponse) + "\n")
    # Login into the emial
    login_statuscode, login_repsonse = smtp.login(FROM, PASSWORD)
    logs.write(str(login_statuscode) + "\n")
    logs.write(str(login_repsonse) + "\n")

    # Attachments
    attachment_path = "./files/send.txt"

    for mail in TO_EMAIL:
        # Compose the email
        msg = MIMEMultipart()
        msg['From'] = FROM
        msg['To'] = mail
        msg['Subject'] = SUBJECT

        # Attach body to the email
        msg.attach(MIMEText(BODY, 'plain'))

        with open(attachment_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name="file.txt")
            part['Content-Disposition'] = f'attachment; filename="{attachment_path}"'
            msg.attach(part)

        try:
            smtp.sendmail(FROM, mail, msg.as_string())
        except:
            error = "Error sending email to " + mail
            logs.write(error + "\n")

    # Closes the connection after sending the emails
    smtp.quit()
    logs.close()