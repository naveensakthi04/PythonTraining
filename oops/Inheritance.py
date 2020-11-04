class Hello:
    def greet(self):
        print("Hello, World!")

    def feature_one(self):
        print(self.__class__, "Feature 1 from Hello")


class A:
    def feature_one(self):
        print(self.__class__, "Feature 1")

    def feature_two(self):
        print(self.__class__, "Feature 2")


# single inheritance
class B(A):
    def feature_three(self):
        print(self.__class__, "Feature 3")

    def feature_four(self):
        print(self.__class__, "Feature 4")


# multilevel inheritance
class C(B):
    def feature_five(self):
        print(self.__class__, "Feature 5")


# multiple inheritance
class D(Hello, A):              # if both the class contain same method signature, priority goes from Left to Right.
    pass                        # in this case, Feature_one of Hello class is called.
                                # This is called as Method Resolution Order


# hierarchical inheritance
class E(A):
    pass

# main()

a = A()
a.feature_one()
a.feature_two()

b = B()
b.feature_one()
b.feature_two()
b.feature_three()
b.feature_four()

c = C()
c.feature_one()

d = D()
d.greet()
d.feature_two()
d.feature_one()

E().feature_one()


