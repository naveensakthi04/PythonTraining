# 14. Write a Python program to find the length of the last word.
# Input : Python Exercises
# Output : 9

def lengthOfLastWord(sentence):
    words = sentence.split(" ")
    if words[len(words)-1] == "":
        words.pop()
    return len(words[len(words) - 1])

sentence = input("Enter a sentence")
result = lengthOfLastWord(sentence)
print(result)