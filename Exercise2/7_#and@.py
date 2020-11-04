# Driver Code
_input = input("Enter the string: ")
for i in range(len(_input)):
    if _input[i] == '#':
        _input = _input[:i] + '@' + _input[i+1:]
    elif _input[i] == '@':
        _input = _input[:i] + '#' + _input[i+1:]

print(_input)
