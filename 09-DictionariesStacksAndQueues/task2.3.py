###
# Removes duplicate email addresses using a set
#
emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]
unique_emails = set(emails)   # zamiana listy na set automatycznie usuwa duplikaty!
print(unique_emails)