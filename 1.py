#1
class StringM:
    def __init__(self):
        self.input_s = ""

    def getS(self):
        self.input_s = input()

    def printS(self):
        print(self.input_s.upper())


stringM = StringM()
stringM.getS()
stringM.printS()