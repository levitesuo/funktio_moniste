from equation import Equation

class Equation_group:
    def __init__(self, equations):
        self.equations = []
        for equation in equations:
            left_side = ""
            right_side = ""
            onRight = False
            for term in equation:
                if "=" in term: onRight = True
                else:
                    if not onRight: left_side  += term
                    else:           right_side += term
            if len(right_side) != 0: self.equations.append(Equation(right_side, left_side))
            else:                    self.equations.append(Equation(left_side))

    def get_latex(self):
        out_strings = []
        for equation in self.equations:
            out_strings.append(equation.get_string())
        return out_strings

    def manipulate_add(self, funcNum, termstr):
        self.equations[funcNum].manipulate_add(termstr)

if __name__ == "__main__":
    eg = Equation_group(["3x 4y 12", "1x 1y 1"])
    print(eg.get_latex())
    eg.manipulate_add(0, "-3x")
    print(eg.get_latex())