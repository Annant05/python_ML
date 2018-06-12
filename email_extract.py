file = open('email.txt')
lines = []
for i in file:
    lines.append(i)
email_from = ""
email_to = ""
email_subject = ""
email_body = ""
for i in lines:
    email_from = i.startswith("From:")
    email_to = i.startswith("To:")
    email_subject = i.startswith("Subject:")
    email_body = i.startswith("Body:")

print(email_from)
print(email_to)
print(email_subject)
print(email_body)
