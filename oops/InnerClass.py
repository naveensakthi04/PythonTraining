class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

        # creating object for inner class inside the class
        self.laptop = self.Laptop()

    def show(self):
        print(self.name, self.roll_no)


    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.ram = "8GB"
            self.rom = "1TB"

        def show(self):
            print(self.brand, self.ram, self.rom)


# main()
student1 = Student("Naveen", 103)
student1.show()

# accessing inner class methods
student1.Laptop().show()

lap1 = student1.Laptop()
lap1.show()

# creating object for inner class outside the class
lap1 = Student.Laptop()
lap1.show()

