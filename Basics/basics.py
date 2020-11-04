import math as M
from math import ceil

print("Hello World!")
print(5 // 2)
print(5 / 2)
print(2 * 7)
print(2 ** 7)
print('Hello World')
print('''Naveen''')
print('''Naveen''')
print("\"Naveen\"")
print(10 * "Naveen ", end=" ")
print(r'\naveen')
x = 10
y = 12
print(x + y)

# split function
print("Hai "+"Hello:World".split(":")[0])


# LIST OPERATIONS => min, max, sum, insert, append, sort, reverse
# LIST OPERATORS => in, not in, :, []
print("------------------------")
print("LIST OPERATIONS")

x = "Hello World"
print(x)
print(x[2:])
print(x[:4])
print(x[2:7])
print(x[-5:])
print("-5 to -9 " + x[-5:-9])
print(x[:-1])
print(x[-1:])
print(x[-1:-1])
print("length of \"" + x + "\" is " + str(len(x)))
print(x[::-1])
print(x[3:7:3])
print("---------------------------------")

nums = [1, 2, 3, "four"]
print(nums)

names = ["hello", "bye", 'all']

nums.extend(names)
print(nums, names)

nums.append(1)
print(nums)

nums.insert(3, "hello")
print(nums)

nums.pop(3)
print(nums)

del nums[3:7]
print(nums)

print(min(nums))

nums.sort()
print(nums)

nums[2] = 120
print(nums)

# nums[24] = 120 //exits with code 1
# print(nums)   no error... but it will not be inserted
#
# LISTS - TUPLE - SET
# mutable - immutable - mutable
# slow - fast - fast
# insertion_order - insertion_order - hash_order
# indexing - indexing - no_indexing
# not_type_specific - not_type_specific - not_type_specific
# duplicates - no_duplicates -
nums = (1, 2, 3)
print(nums)

print(nums[2])

tup = (12, 14, 15, "hello", 12)

print(tup)

set0 = {1, 6, 4, 2, 4, "Hello"}
print(set0)

# set[2] //not possible

a = True
print(not a)

# SET OPERATIONS => union, intersection, difference, symmetric_difference
print("------------------------")
print("SET OPERATIONS")

# remove() throws error if specified item is not present
# discard() removes item if it is present, else nothing happens


a = {101, 2, 63, 4, 5, "a"}
b = {4, 5, 6, 7, 8, 'a'}
print("before poping")
print(a)
a.pop()
print("poping")
print(a)

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

print(a)
print(b)

a.difference_update(b)
print(a)

b.symmetric_difference_update(a)
print(b)

# DICTIONARY OPERATIONS =>

# key = immutable : value = mutable
print("------------------------")
print("DICTIONARY OPERATIONS")

captains = {'England': 'Root', 'Australia': 'Smith', 'India': 'Virat', 'Pakistan': 'Sarfraz'}
print(captains.keys())
print(captains.values())
print(captains["England"])

del captains['England']
print(captains)

captains["Australia"] = "Finch"

print(captains)
print(min(captains))

s1 = {"name": "Nitsh", "age": 21, "marks": 60}
s2 = {"name": "Naveen", "age": 21, "marks": 80}
s3 = {"name": "Sarvesh", "age": 21, "marks": 90}

interns = {1: s1, 2: s2, 3: s3}

print(interns)
print(interns[1]["marks"])

print(len(interns))
print(len(interns[2]))

print("------------------------------------")
print("ID")

a = 10
b = 10
print("a = 10 b = 10 ")
print(id(a))
print(id(b))
print(id(10))
print("id(9)", end=" ")
print(id(9))

print("a = 11")
a = 11
print(id(a))
print(id(b))

print(a.__sizeof__())
a = "STRING"
print(a.__sizeof__())
a = "s"
print(a.__sizeof__())

# ::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::\./::::::::::::::::::::::
# :::::::::::::::.\.::::::::::::::::::::::
# :::::::::::::::/.\::::::::::::::::::::::
# :::UNFORTUNATELY NO CONSTS IN PYTHON::::
# ::::::::::::::::::::::::::::::::::::::::

print("DATATYPES")
print(type(a))
print(type(captains))
print(type(nums))
print(type(None))
print(type(1 + 3j))
print(type(False))

a = 5
print(complex(a))

print(type(a))
print(type(float(a)))

print(bool(4))
print(bool(-4))
print(bool(0))

a = range(2, 10, 3)
print(a)
a = list(range(2, 10, 3))
print(a)
a = tuple(range(2, 10, 3))
print(a)
a = set(range(2, 10, 3))
print(a)

print("----------------------------")
print("OPERATORS")

x = 1
x += 2
print(x)

m, n = 1, 6
print(m, n)

m, n = n, m
print(m, n)

# and or not
# > < == <= >= !=
# ~ & | ^ << >>
print(~13)

# MATH FUNCTIONS

print(M.factorial(12))
a = ceil(1.1)
print(a)

# INPUT
# Converting from float rep as string to int
# x = int(float(input("Enter a number")))
# print(x)
#
# x = input("Enter a char")[0]
# print(x)
#
# x = eval(input("Enter a expr"))
# print(x)

# for command line input
# import sys
# x = sys.argv[1]


print("------------------------------------------")
print("Type Conversion")

print("bool(\"\")")
print(bool(""))
print("bool(\"False\")")
print(bool("False"))


# CONDITIONAL STATEMENTS
print("--------------------------------------------")
print("CONDITIONAL STATEMENTS")

if 1000 < 100:
    print("10 is less than 100")
else:
    if 100 == 12:
        print("Hello")
    elif (100 > 12):  # parenthesis is optional
        print("Hello all")
    else:
        print("Welcome")

# LOOPS
print("--------------------------------------------")
print("LOOPS")

num = 0
while num < 5:
    num = num + 1
    print("num =", num)
else:
    print("END")

for x in range(1, 4):
    print("Hello", end="")
    for y in range(x, 15, 3):
        print(" World" + str(y), end="")
    print()

dict = {1: 100, 2: 200, 3: 300}
for k in dict.keys():
    print(k, dict.get(k))

for k in dict.items():
    print(k)

for k, v in dict.items():
    print(k, v)

# break - exits loop
# continue - skips current iteration
# pass - does nothing... not considered as a statement by the interpreter

# FUNCTIONS
print("----------------------------------")
print("FUNCTIONS")


def add_sub(_1, _2):
    _a = _1 + _2
    _b = _1 - _2
    return _a, _b


s, m = add_sub(10, 56)
print("check")
print(m)
print(s)


def greet(name):
    print("Hello" + " " + name)
    return


greet("Naveen")

# for immutable objects python is call by value like thing... not exactly
# for mutable objects python call by reference
print("CALL BY VALUE OR REFERENCE")

print("IMMUTABLE")


def update_immutable(x):
    print(id(x))
    x = 20
    print(id(x))
    print(x)
    return


x = 10
print(id(x))
print(x)
update_immutable(x)
print(x)

print("MUTABLE")


def update_mutable(x):
    print(id(x))
    x[1] = 21
    print(id(x))
    print(x)
    return


x = [10, 20, 30]
print(id(x))
print(x)
update_mutable(x)
print(x)


# TYPES OF ARGUMENTS
# POSITION is the default

# KEYWORD
def person(name, age):
    print(name)
    print(age)


person(age=21, name="Naveen")


# DEFAULT
def person1(name, age=30):
    print(name)
    print(age)


person1(name="Naveen")

# VARIABLE LENGTH
def addVarialbeLength(*x):
    _s = 0
    for i in x:
        _s += i
    print("sum=", end=" ")
    print(_s)

addVarialbeLength(5,6,7,8,9)

# KEYWORDED VARIABLE LENGTH ARGUMENTS

def _person(**x):

    for i,j in x.items():
        print(i,j)

_person(name="Naveen", age="21", city="Coimbatore")
