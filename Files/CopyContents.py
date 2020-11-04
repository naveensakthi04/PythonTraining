# input_file = open("input.txt", "r")
# output_file = open("output.txt", "w")
# output_file.write(input_file.read())
#
# input_file.close()
# output_file.close()
#
#
# input_img_file = open("img.png", "rb")
# output_img_file = open("out_img.jpeg", "wb")
#
# input_img_file.close()
# output_img_file.close()


import os


def add(a, b):
    return a+b


# open("out_img.jpeg", "wb").write(open("img.png", "rb").read())

def main():
    input_file_name = "input.txt"
    file_stats = os.stat(input_file_name)
    print(file_stats)


if __name__ == "__main__":
    main()

# with open("jsonfile.json","r") as f:          ///Opening files this way automatically closes the file if exception occurs
# with open("jsonfile.json","w") as f:
#     json.dump(my_data,f)
# f.close()




######  ##### #    # ######  ########
#     # #   # #    # #     #    #
#     # #   # #    # ######     #
#     # #   # #    # #     #    #
######  ##### ###### ######     #


# write() method doesn't write data to a file, but to a buffer, it does, but only when the close() method is called.
# This latter method flushes the buffer and writes the content to the file.
# If you wish not to close the file using fileObject.flush() method to clear the buffer and write back to file.