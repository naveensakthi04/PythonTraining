import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

HaHa Ha

Metacharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

www.helloworld.com
wwwfhelloworld5com


994-243-6762
861.086.7187

Mr. Pythonabc
Mr Pycharm
Ms Jetbrains
Mrs. Python

cat
bat
mat
pat

'''

sentence = "Start a sentence and bring it to an end"

# pattern = re.compile(r'abc')
# matches = re.finditer(pattern, text_to_search)  # returns: <re.Match object; span=(139, 140), match='abc'>, all occurrences
# matches = re.findall(pattern, text_to_search)   # returns: abc, all occurrences
# matches = re.search(pattern, text_to_search)    # returns: abc, only the first occurrence
# matches = re.match(pattern, text_to_search, re.IGNORECASE)    # returns: abc, searches only at the beginning of the string
#
# for match in matches:
#     print(match)

# pattern = re.compile(r"\.")  # dot matches with all characters except \n... so use "\." instead of "."

# pattern = re.compile(r"www.helloworld.com")  # dot matches with almost all characters... so use "\." instead of "."

# pattern = re.compile(r"\bHa")   # matches the instances after word boundary

# pattern = re.compile(r"\BHa") # matches not the instances after word boundary


# pattern = re.compile(r"^Start") # beginning of the string
# pattern = re.compile(r"end$") # end of the string


# pattern = re.compile(r"[9]\d{2}[-.]\d{3}[.-]\d{4}")

# pattern = re.compile(r"[^b]at")

# pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)


urls ='''
https://www.google.com
https://facebook.com
http://youtube.net
http://www.python.org
'''

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
matches = pattern.finditer(urls)

subbed_urls = pattern.sub(r'\2\3', urls)

print(urls, subbed_urls)
for match in matches:
    print(match.group(2))
