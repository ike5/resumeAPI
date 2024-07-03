import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    sender_email = os.getenv("EMAIL")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    password = os.getenv("PASSWORD")  # Use environment variable or secure vault for storing passwords

    # Create the email content
    message = MIMEMultipart("alternative")
    message["Subject"] = "Test Email"  # todo: submit form email here
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    This is a test email.
    """
    part1 = MIMEText(text, "plain")

    # Attach parts into message container
    message.attach(part1)

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP authentication error: {e}")
    except smtplib.SMTPRecipientsRefused as e:
        print(f"Recipient address rejected: {e}")
    except smtplib.SMTPSenderRefused as e:
        print(f"Sender address rejected: {e}")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")


if __name__ == "__main__":
    main()
