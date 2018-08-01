# validate_email.py

"""
You are given an integer followed by email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.

Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The maximum length of the extension is 3.
"""
from string import ascii_letters, digits

RIGHT_UNAME = set(ascii_letters)
RIGHT_UNAME.update(digits)
RIGHT_UNAME.add("-")
RIGHT_UNAME.add("_")


def check_username(uname):
    res = False
    if uname and all((x in RIGHT_UNAME for x in uname)):
        res = True
    return res


def check_website(site):
    return site.isalnum()


def check_ext(ext):
    res = True
    size = len(ext)
    if not (1 < size <= 3):
        res = False
    if not ext.isalpha():
        res = False
    return res


def fun(s):
    res = True
    try:
        uname, web_site = s.split("@")
        if not check_username(uname):
            res = False
        else:
            web_site, ext = web_site.split(".")[:2]
            if not all([check_website(web_site), check_ext(ext)]):
                res = False

    except Exception:
        res = False
    finally:
        return res


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == "__main__":

    n = int(input().strip())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
