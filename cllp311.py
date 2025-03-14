class Project:
    def __init__(self, design, code, debug, test):
        self.design = (design)
        self.code = (code)
        self.debug = (debug)
        self.test = (test)
        self.whole = 0
        self.percentdesign = 0
        self.percentcode = 0
        self.percentdebug = 0
        self.percenttest = 0

    def percentCalc(self):
        self.whole = self.design + self.code + self.debug + self.test
        self.percentdesign = self.design / self.whole
        self.percentcode = self.code / self.whole
        self.percentdebug = self.debug / self.whole
        self.percenttest = self.test / self.whole

    def __str__(self):
        return f"Task \t\t %Time\nDesigning\t\t{100*self.percentdesign}%\nCoding\t\t\t{100*self.percentcode}%\nDebugging\t\t{100*self.percentdebug}%\nTesting\t\t\t{100*self.percenttest}%"



