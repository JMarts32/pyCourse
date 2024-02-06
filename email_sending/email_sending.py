from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta, date
import time
import smtplib
import getpass
import sched


def snd_mail(from_mail, password):
    HOST = "smtp-mail.outlook.com"
    PORT = 587

    TO_EMAIL = ["jm2002.santosa@gmail.com"]

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
    login_statuscode, login_repsonse = smtp.login(from_mail, password)
    logs.write(str(login_statuscode) + "\n")
    logs.write(str(login_repsonse) + "\n")

    # Attachments
    attachment_path = "./files/send.txt"

    for mail in TO_EMAIL:
        # Compose the email
        msg = MIMEMultipart()
        msg['From'] = from_mail
        msg['To'] = mail
        msg['Subject'] = SUBJECT

        # Attach body to the email
        msg.attach(MIMEText(BODY, 'plain'))

        with open(attachment_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name="file.txt")
            part['Content-Disposition'] = f'attachment; filename="{attachment_path}"'
            msg.attach(part)

        try:
            smtp.sendmail(from_mail, mail, msg.as_string())
        except:
            error = "Error sending email to " + mail
            logs.write(error + "\n")

    # Closes the connection after sending the emails
    smtp.quit()
    logs.close()

def calculate_next_send(hour, minutes, seconds):
    # Get the current time
    now = datetime.now()

    # Set the desired time for the next time of sendind emails
    next_run = datetime(now.year, now.month, now.day, hour, minutes, seconds)

    # If the next run time is in the past, schedule it for the next day
    if now > next_run:
        next_run += timedelta(days=1)

    # Return the next run time as a timestamp
    return time.mktime(next_run.timetuple())

# Create a scheduler
s = sched.scheduler(time.time, time.sleep)

print("Welcome to the automatic sending email software :D")

print("\nPlease make sure that the email is from microsoft :D")
from_mail = input("Enter the email where you are sending the emails: ")
password = getpass.getpass("Enter the password: ")

decision = input("Do you want to schedule? (Y/N): ")

if decision.lower() == "y":
    try: 
        hour = int(input("\nEnter the hour where you want to send the emails: "))
        minutes = int(input("Enter the minutes where you want to send the emails: "))
        seconds = int(input("Enter the seconds where you want to send the emails: "))
    except:
        print("The time must be a numerical value in the 24 hour format")

    print("\n The mails are goinr to be sent at", str(hour) + ":" + str(minutes) + ":" + str(seconds))

    s.enterabs(calculate_next_send(hour, minutes, seconds), 1, snd_mail(from_mail,password), ())

    # Start the scheduler
    s.run()
elif decision.lower() == "n":
    snd_mail(from_mail,password)
else:
    print("\nno valid selection")