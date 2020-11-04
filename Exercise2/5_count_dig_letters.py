def count(str):
    digit_count = 0
    letter_count = 0
    for s in str:
        if s.isdigit():
            digit_count += 1
        elif s.isalpha():
            letter_count += 1
    return digit_count, letter_count


# Driver code
_input = input("Enter the string: ")
digits, letters = count(_input)
print("Digits: ", digits)
print("Letters: ", letters)
