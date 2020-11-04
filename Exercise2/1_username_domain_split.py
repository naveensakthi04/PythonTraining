import re

email_pattern = r"[a-zA-Z]+[0-9]*[a-zA-Z]*@[a-zA-Z]+\.[a-zA-Z]+"


def check_email(email):
    global email_pattern
    pattern = re.compile(email_pattern)
    match = pattern.findall(email)

    if len(match) != 1:
        print("Invalid email")
        return False

    return True


def get_email():
    email = input("Enter email: ")
    check = check_email(email)
    if check:
        return email
    else:
        return get_email()


def split_email(email):
    email = email.split("@")
    return email[0], email[1]


# Driver Code
email = get_email()
username, domain = split_email(email)
print("Username: ", username)
print("Domain: ", domain)



