def email_list(domains):
  emails = []
  a=[]
  for email,users in domains.items():
    for user_name in users:
      a =user_name + "@"+email
      emails.append(a)
  return(emails)

print(email_list({"gmail.com": ["charlie.aeron", "harry.prince", "peter.beck"], "yahoo.com": ["sara.micheal", "jean.jonh"], "hotmail.com": ["leo.jordi"]}))
