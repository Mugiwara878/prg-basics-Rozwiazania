###
# Finds spam emails using set intersection
#
emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
spam_list = {"spam1@example.com", "spam2@example.com"}

spam_emails = emails_received & spam_list   # część wspólna: co jest w OBU zbiorach naraz
print("Spam emails:", spam_emails)