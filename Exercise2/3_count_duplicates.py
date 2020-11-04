import re
def get_dupes(filename):
    dupes = dict()
    content = ""
    with open(filename, "r") as f:
        content = f.read()
        content = content.strip()
        content = content.lower()
        content = re.findall("\w+", content)
        # content = content.split(r"[^a-zA-Z0-9']")

    for i in range(len(content)):
        if dupes.__contains__(content[i]):
            dupes.update({content[i]: int(dupes.get(content[i])) + 1})
        else:
            dupes.update({content[i]: 1})
    return dupes


# Driver code
filename = input("Enter file name: ")
dupes = get_dupes(filename)
for k, v in dupes.items():
    if v > 1:
        print(k, v)



