# in classes, variables are of two types, Class/Static and Instance variables
# methods are of three types, class method: works with class variables, instance method: works with instance variables
# and static method: has nothing to do with variables

class Computer:
    hasOS = True                   # outside __init__() static or class variable

    # Constructor
    def __init__(self, ram, rom):  # self is similar to this keyword
        print("This is init")
        self.ram = ram             # inside __init__ instance variable
        self.rom = rom

    def config(self):
        print("This is config", end=": ")
        print(self.ram, self.rom)

    def compare(self, other):
        return self.ram == other.ram and self.rom == other.rom

    @classmethod                    # class methods must be defined this way
    def has_os(cls):
        print("Has OS: ",cls.hasOS)


    @staticmethod
    def greet():
        print("Hello All")

# main

# Computer.config(Computer("4GB", "500GB"))

computer = Computer
# computer.config(computer("4GB", "500GB"))

Computer.greet()
com1 = Computer("4GB", "500GB")
Computer.config(com1)

com2 = computer("8GB", "1TB")
com2.config()

com3 = computer("8GB", "1TB")
com3.config()

print("com1 == com2 ", com1.compare(com2))
print("com2 == com3", com2.compare(com3))

# print("HasOS: ", Computer.hasOS)
# print("HasOS: ", com1.hasOS)
# print("HasOS: ", com2.hasOS)

Computer.has_os()

