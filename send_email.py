# File: notifications/send_email.py
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = 'yourEmail@example.com'
    password = 'yourEmailPassword'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    send_email('Task Reminder', 'This is a reminder for your upcoming task.', 'recipient@example.com')
