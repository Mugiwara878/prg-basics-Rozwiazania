###
# Functions to extract information from a raw email
#
import re

def email_sender(text):
    match = re.search(r'From:.*<(.+?)>', text)   # szuka linii "From:...", wyciąga to co w <>
    return match.group(1)

def email_recipient(text):
    match = re.search(r'To:.*<(.+?)>', text)
    return match.group(1)

def email_subject(text):
    match = re.search(r'Subject: (.+)', text)     # wyciąga resztę linii po "Subject: "
    return match.group(1)

def email_body(text):
    parts = text.split('\n\n', 1)    # dziel tekst na nagłówki/treść przy PIERWSZEJ pustej linii
    return parts[1].strip() if len(parts) > 1 else ''