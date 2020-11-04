# Note:  Python does not support method overloading
class A:
    def show(self):
        print("in A")

    def show(self, str):            # now the previous show() methods are not available for use.
        print(str, ", Hello")


class B(A):
    def show(self):                 # not Overriding because the this A.show() is removed from the memory, only A.show(str) is available
        print("in B")





# main()
B().show()
# A().show()                        # this line throws an error
A().show("STR")
