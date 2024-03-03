import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email():
    try:
        # infos
        smtp_server = input("Enter SMTP server address: ")
        smtp_port = int(input("Enter SMTP server port (e.g., 587 for TLS): "))
        username = input("Enter your email address: ")
        password = input("Enter your email password: ")
        recipient = input("Enter the recipient's email address: ")
        subject = input("Enter the email subject: ")
        body = input("Enter the email body: ")
        times = int(input("Enter how many times you want to send the email: "))

        message = MIMEMultipart()
        message['From'] = username
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # connect
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)

        for i in range(times):
            server.sendmail(username, recipient, message.as_string())
            print(f"Email sent {i + 1} times")

        server.quit()

    except ValueError:
        print("Error: Please enter a valid integer for the port and number of times.")

    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Please check your email address and password.")

    except smtplib.SMTPConnectError:
        print("Error: Connection to the SMTP server failed. Please check the server address and port.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


send_email()
