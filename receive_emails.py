import email
import imaplib

EMAIL = 'hacktues9assap@gmail.com'
PASSWORD = 'okgexyrallzbuhcp'
SERVER = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
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