from function import Function

class Equation:
    def __init__(self, left_side, right_side = "0"):
        self.left = Function(left_side)
        self.right = Function(right_side)
    
    def get_latex(self):
        return f"\({self.left.get_latex()}={self.right.get_latex()}\)"
    
    def get_string(self):
        return f"{self.left.get_latex()}={self.right.get_latex()}"
    
    def manipulate_add(self, termstr):
        self.right.manipulate_add(termstr)
        self.left.manipulate_add(termstr)

if __name__ == "__main__":
    e = Equation("10 3x 7y")
    print(e.get_latex())
    e.manipulate_add("3x")
    print(e.get_latex())
    e.manipulate_add("-7y")
    print(e.get_latex())