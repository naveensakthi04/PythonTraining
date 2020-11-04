class A:
    def __init__(self):
        print(self.__class__, "init from A")

    def feature_one(self):
        print(self.__class__, "Feature 1")

    def feature_two(self):
        print(self.__class__, "Feature 2")


class B(A):
    def feature_three(self):
        print(self.__class__, "Feature 3")

    def feature_four(self):
        print(self.__class__, "Feature 4")


class C(A):
    def __init__(self):
        print(self.__class__, "init from C")

    def feature_three(self):
        print(self.__class__, "Feature 3")

    def feature_four(self):
        print(self.__class__, "Feature 4")


class D(A):
    def __init__(self):
        print(self.__class__, "init from D")
        super().__init__()                      # super need not be as the first statement

    def feature_three(self):
        print(self.__class__, "Feature 3")

    def feature_four(self):
        print(self.__class__, "Feature 4")


# main()
A()
B()
C()
D()
