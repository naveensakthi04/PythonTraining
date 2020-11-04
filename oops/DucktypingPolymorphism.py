# Duck typing... The Class or the type of the object is not important, rather the if the class contains the method or not is important

class Pycharm:
    def __init__(self):
        self.name = "PyCharm Pro"

    def show(self):
        print(self.name)


class Eclipse:
    def __init__(self):
        self.name = "Eclipse"

    def show(self):
        print(self.name)


class Language:
    def __init__(self, name, ide):  # Type of ide is not important.
        self.name = name
        self.ide = ide

    def show(self):
        print(self.name)
        self.ide.show()  # Only concern is that ide has show() method or not.


# main
# ide = Pycharm()
ide = Eclipse()
python = Language("Python", ide)
python.show()
