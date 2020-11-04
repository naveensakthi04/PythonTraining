# Operator Overloading
# Each operator is assigned to a function internally.
# For example, 5 + 9 internally calls int.__add__(a, b)
# Overloading the method assigned with that operator is called as operator overloading.

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        return Student(self.m1 + other.m1, self.m2 + other.m2)

    def __gt__(self, other):
        return self.m1 + self.m2 > other.m2 + other.m2

    def __str__(self):                          # like toString() in java
        return str(self.m1) + " " + str(self.m2)


# main()
s1 = Student(45, 55)
s2 = Student(55, 60)

print(s1 + s2)              # internally calls Student.__str__(Student.__add__())

if s1 > s2:
    print("s1 scored more marks")
else:
    print("s2 beats s1")
