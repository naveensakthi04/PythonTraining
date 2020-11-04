import re


def get_counts(filename):
    line_count = 0
    word_count = 0
    with open(filename, "r") as f:
        line = f.readline()
        while line != "":
            line_count += 1
            word_count += len(re.findall(r'\w+', line))
            line = f.readline()

    return line_count, word_count


# Driver code
filename = input("Enter file name: ")
line_count, word_count = get_counts(filename)
print("number of lines: ", line_count)
print("number of words: ", word_count)
