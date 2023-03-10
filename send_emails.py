from email.message import EmailMessage
import ssl
import smtplib
import imghdr
import email
import imaplib
import time

email_sender = 'hacktues9assap@gmail.com'
email_password = 'okgexyrallzbuhcp'
email_receiver = 'alexhristov2005@gmail.com'

subject = 'Dano se poluchi toq put'

SERVER = 'imap.gmail.com'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content('')

with open("image.jpg", "rb") as image:
    file_data = image.read()
    file_type = imghdr.what(image.name)
    file_name = image.name

em.add_alternative(""""\
<!DOCTYPE html>
<html>
    <head>
        <script>
            if(document.getElementById('da').clicked() == true) {
                alert("DA");
            }

            if(document.getElementById('ne').clicked() == true) {
                alert("NE");
            }
        </script>
    </head>

    <body>
        <button><a style = "text-decoration: none; color: darkgray;" href="mailto:hacktues9assap@gmail.com?subject=Security&body=Yes">Yes</a></button>
        <br>
        <br>
        <button><a style = "text-decoration: none; color: darkgray;" href="mailto:hacktues9assap@gmail.com?subject=Security&body=No">No</a></button>
    </body>
</html>

""", subtype = 'html')

em.add_attachment(file_data, maintype = "image", subtype = file_type, filename = file_name)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

#recvive

time.sleep(20)

mail = imaplib.IMAP4_SSL(SERVER)
mail.login(email_sender, email_password)
mail.select('inbox')
status, data = mail.search(None, 'FROM "alexhristov2005@gmail.com"')
mail_ids = []

for block in data:
    mail_ids += block.split()

status, data = mail.fetch(mail_ids[-1], '(RFC822)')
for response_part in data:
    if isinstance(response_part, tuple):
        message = email.message_from_bytes(response_part[1])
        if message.is_multipart():
            mail_content = ''

            for part in message.get_payload():
                if part.get_content_type() == 'text/plain':
                    mail_content += part.get_payload()
        else:
            mail_content = message.get_payload()

        print(f'Content: {mail_content}')
        