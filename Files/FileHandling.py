file = open("data.txt", "r")


#print(file.read())


# line = file.readline()
# while line != "":
#     print(line, end="")
#     line = file.readline()



# lines = file.readlines()
# while lines != "":
#     print(lines, end="")
#     print("check")
#     lines = file.readline()


while True:
        try:
            line=next(file)
            print (line,end="")
        except StopIteration:
            break

print()
print("Current position", end=" ")
print(file.tell())

file.seek(0,0)

print()
print("Current position", end=" ")
print(file.tell())



file = open("data.txt", "a+")
file.write("This is file appending\n")
file.seek(0,0)

print("READING")
print(file.read())


file = open("data.txt", "w+")
file.write("This is file writing\n")
file.seek(0,0)

print("READING")
print(file.read())