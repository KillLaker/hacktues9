from email.message import EmailMessage
import ssl
import smtplib
import imghdr

email_sender = 'hacktues9assap@gmail.com'
email_password = 'okgexyrallzbuhcp'
email_receiver = 'alexhristov2005@gmail.com'

subject = 'Dano se poluchi toq put'
body = """
MOLQ TE BOJE!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

with open("image.jpg", "rb") as image:
    file_data = image.read()
    file_type = imghdr.what(image.name)
    file_name = image.name

em.add_attachment(file_data, maintype = "image", subtype = file_type, filename = file_name)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    