import emails

with open('email.txt', 'r') as file:
    content = file.read()

print('Sender:', emails.email_sender(content))
print('Recipient:', emails.email_recipient(content))
print('Subject:', emails.email_subject(content))
print('Body:')
print(emails.email_body(content))
