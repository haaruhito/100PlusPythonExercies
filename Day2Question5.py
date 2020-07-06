# Define a class which has at least two methods:

        # getString: to get a string from console input
        # printString: to print the string in upper case.

    # Also please include simple test function to test the class methods.

class StringExample:
    def getString(self):
        self.s = input("Enter an string: ")

    def printString(self):
        print (self.s.upper())



Object1 = StringExample()

Object1.getString()
Object1.printString()

