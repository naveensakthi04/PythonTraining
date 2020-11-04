# Python dont have abstract class on its own
# so,

from abc import ABC, abstractmethod


# ABC - Abstract Base Class


# normal class can have abstract methods
# class A:
#
#     @abstractmethod
#     def abs_method(self):
#         print("Hello")
#
#
# A().abs_method()


# abstract classes may or may not have abstract methods
# class A(ABC):
#
#     def abs_method(self):
#         print("Hello")
#
#
# A().abs_method()
#


# class A(ABC):
#
#     def abs_method(self):
#         print("Hello")
#
#
# # Abstract class with non abstract methods can be instantiated
# A().abs_method()


# class A:
#
#     # abstract method may or may not have definition
#     @abstractmethod
#     def abs_method(self):
#          print("Hello")
#
#
# class B(A):
#     pass
#
#
# B().abs_method()


# Therefore, a class is abstract iff it extends ABC and has an abstract method
# class A(ABC):
#
#     # abstract method may or may not have definition
#     @abstractmethod
#     def abs_method(self):
#         pass
#
#
# class B(A):
#     def abs_method(self):
#         print("Hello")
#
#
# B().abs_method()


# multilevel abstraction


class A(ABC):
    @abstractmethod
    def abs_method1(self):
        pass

    @abstractmethod
    def abs_method2(self):
        pass


class B(A):
    def abs_method1(self):
        print("abs1")


class C(B):
    def abs_method2(self):
        print("abs2")


# main()
# B().abs_method1()  # throws error. Though not specified abstract...
# not implementing all the methods of base class makes B abstract implicitly
C().abs_method1()
C().abs_method2()
