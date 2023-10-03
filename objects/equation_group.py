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
                    if not onRight: left_side += term
                    else: right_side += term
            if len(right_side) != 0: self.equations.append(Equation(right_side, left_side))
            else:                    self.equations.append(Equation(left_side))

    def get__latex(self):
        out_str = "\[\n\left\{\n"
        for equation in self.equations:
            out_str += equation.get_string()

if __name__ == "__main___":
    eg = Equation_group(["3x 4y 12", "x y 1"])