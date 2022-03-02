import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL
password = "test4collyers01!"
login = "test4collyers@gmail.com"


def sendMail(recieverEmail, usrPass):
    message = MIMEMultipart()
    message["Subject"] = "Keisen Judo password reset"
    message["From"] = login
    message["To"] = recieverEmail

    # Create the HTML part of your email

    text = """\
<!-- #######  YAY, I AM THE SOURCE EDITOR! ######### -->
<h1 style="color: #5e9ca0;" data-darkreader-inline-color=""><img src="https://i.imgur.com/eDBuaQ0.png" alt="" /></h1>
<h1>Keisen Judo thanks you for using our tracker</h1>
<h2 style="color: #5e9ca0;" data-darkreader-inline-color="">Your password has been reset:</h2>
<p><strong>A temporary password has been set.</strong></p>
<p>Your temporary password: <span style="background-color: #2b2301; color: #fff; display: inline-block; padding: 3px 10px; font-weight: bold; border-radius: 5px;" data-darkreader-inline-bgcolor="" data-darkreader-inline-color="">'{}'</span></p>
<p><strong>&nbsp;</strong></p>""".format(usrPass)

    print(text)

    part1 = MIMEText(text, "html")

    message.attach(part1)

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Tries to send the email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(login, password)

            # SEND EMAIL HERE

            server.sendmail(login, recieverEmail, message.as_string())

            print("Sending mail to " + recieverEmail)
            return True

    except smtplib.SMTPRecipientsRefused as e:
        print(e)
        return False


if __name__ == "__main__":
    sendMail("liam.palmqvist@icloud.com", "Hello")
