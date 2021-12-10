import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# These libraries will allow you to send emails with multiple parts and attatchments

port = 465  # For SSL
login = "test4collyers@gmail.com"  # The email address you will be using to send the email. This needs to be a gmail account as the port used is for gmail
password = "test4collyers01!"  # This is the password to the account you will be using to send your email
# WARNING #
'''
In order to send emails with a gmail account, you need to turn on "allow less secure apps" at https://myaccount.google.com/lesssecureapps
Less secure apps need two factor authentication turned ON for the app to be able to access the email account
'''


def sendMail(recieverEmail, subject, text, image):
# The reciever email, subject and text will need to be in quotes
# the image name and extension will also need to be in quotes and is case sensitive e.g: "Image.png"
# Image can also be Null

    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = login
    message["To"] = recieverEmail

    # Create the plain text part of your email

    part1 = MIMEText(text, "plain")  # This will encode the text to fit in the context of the email

    message.attach(part1)  # Attatches the first part of the text to the email

    if image != None:
        with open(image, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode the file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "content-Disposition",
            f"attachment; filename= {image}",
        )

        message.attach(part)

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(login, password)

        # SEND EMAIL HERE

        server.sendmail(login, recieverEmail, message.as_string())

        print("Sending mail to " + recieverEmail)


if __name__ == "__main__":  # This tests the program when run as a standalone
    login = "test4collyers@gmail.com"  # email to sign in with
    password = "Theswede02!"  # Password for email

    sendMail("liam.palmqvist@icloud.com", "Hello", "ur mom", "assets\logographic.png")
    # Enter your email address, header and message here (optional: add an image with filename and extension)
