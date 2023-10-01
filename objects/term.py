class Term:
    def __init__(self, termstr):
        print("T: ", termstr)
        self.factor = ""
        self.variable = ""
        for char in termstr:
            if char == "x" or char == "y" or char == "z": self.variable = char
            else: self.factor += char

    
    def get_power(self):
        if len(self.variable) == 0: return 0
        best = 1
        for char in self.variable:
            if char.isdigit() and int(char) > best: best = int(char)
        return best
    
    def get_latex(self):
        if len(self.factor) != 0 and int(self.factor) > 0 and not "+" in self.factor and not "-" in self.factor: 
            return "+" + self.factor + self.variable
        else:
            return self.factor + self.variable

if __name__ == "__main__":
    from random import randint as r
    a = Term("7y")
    print(a.get_power())
    print(a.get_latex())
    
