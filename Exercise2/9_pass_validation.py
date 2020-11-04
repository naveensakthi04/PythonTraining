import re


def validate(input):
    up = r"[A-Z]+"
    lo = r"[a-z]+"
    num = r"\d+"
    spe = r"[#$@]+"
    min_len = 6
    max_len = 12

    fails = []
    val = True
    if len(input) < min_len or len(input) > max_len:
        fails.append("Password should of length 6 to 12")
        val = False

    pattern = re.compile(up)
    match = re.search(pattern, input)
    if match is None:
        fails.append("atleast 1 uppercase required")
        val = False

    pattern = re.compile(lo)
    match = re.search(pattern, input)
    if match is None:
        fails.append("atleast 1 lowercase required")
        val = False

    pattern = re.compile(num)
    match = re.search(pattern, input)
    if match is None:
        fails.append("atleast 1 number required")
        val = False

    pattern = re.compile(spe)
    match = re.search(pattern, input)
    if match is None:
        fails.append("atleast 1 special symbol in (@,#,$) required")
        val = False

    for fail in fails:
        print(fail)

    return val


# Driver code
_input = input("Enter password: ")
while not validate(_input):
    print("Keep a better password.")
    _input = input("Enter password: ")
else:
    print("Successful")
