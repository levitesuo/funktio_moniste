class Term:
    def __init__(self, termstr):
        self.factor = ""
        self.variable = ""
        for char in termstr:
            if char == "x" or char == "y" or char == "z": self.variable = char
            else: self.factor += char

    def __add__(self, other):
        if type(other) != type(self):
            print("Both of the operators must be terms")
            return None
        if other.variable != self.variable:
            print("The variables must be the same on both of the terms")
            return None
        return Term(str(int(self.factor) + int(other.factor))+self.variable)
        
    def get_power(self):
        if len(self.variable) == 0: return 0
        best = 1
        for char in self.variable:
            if char.isdigit() and int(char) > best: best = int(char)
        return best
    
    def get_latex(self):
        if int(self.factor) == 1 and len(self.variable) != 0:
            if len(self.factor) != 0 and int(self.factor) > 0 and not "+" in self.factor and not "-" in self.factor: 
                return "+" + self.variable
            else:
                return "+" + self.variable
        elif int(self.factor) == -1 and len(self.variable) != 0:
            if len(self.factor) != 0 and int(self.factor) > 0 and not "+" in self.factor and not "-" in self.factor: 
                return "+" + self.variable
            else:
                return "-"+self.variable
        else:
            if len(self.factor) != 0 and int(self.factor) > 0 and not "+" in self.factor and not "-" in self.factor: 
                return "+" + self.factor + self.variable
            else:
                return self.factor + self.variable

if __name__ == "__main__":
    a = Term("-7x")
    print(a.get_power())
    print(a.get_latex())
    a + Term("3x")
    print(a.get_latex())
    b = Term("1x")
    print(b.get_latex())
    print(b.factor)
    
